"""Klasser for QR-code generator."""
from rute_definisjoner import coordinates, data_coordinates, formatting_data_upper_left, formatting_data_right
import reedsolo

class Rute:
    def __init__(self,i,j,x,y,bredde,tag="rute"):
        self.x = x
        self.y = y
        self.fill = "white"
        self.outline = "black"
        self.w = bredde
        self.tag = tag
        self.id = f"{i},{j}"
        self.rect = None

    def tegnRute(self,canvas):
        self.rect = canvas.create_rectangle(
            self.x - self.w/2,
            self.y - self.w/2,
            self.x + self.w/2,
            self.y + self.w/2,
            fill=self.fill,
            outline=self.outline,
            tags=self.tag,
        )
    
    def isPressed(self, x, y, canvas):
        # Trekker fra bredden til outline så man ikke kan klikke mellom to celler.
        if self.x+1-self.w/2 <= x <= self.x-1 + self.w/2 and \
            self.y+1-self.w/2 <= y <= self.y-1+self.w/2:
            # Flipper fargen
            if self.fill == "white":
                self.fill = "black"
                self.fill = "red"
            else:
                self.fill = "white"
            canvas.itemconfig(self.rect, fill=self.fill, outline=self.outline)
            return self.id
        else:
            return False

class QR_generator:
    """
    1. Text to binary
    2. Reed-Solomon error encoding of the text
    3. Write the data fields in QR code.
    4. Apply the 8 different masks to the code and calculate the penalty.
    5. Choose the lowest penalty mask and apply it to the data fields.
    6. Create format string: Error correction level and mask version 0-7.
    7. Reed-Solomon error encoding of the format string: 5-bit + 10-bit error correction.
    8. XOR the format string with the 15-bit fixed mask 101010000010010.
    9. Write the masked format string to QR code.
    10. Done!

    Error correction levels.
    01 = Level L (Low - ~7% error correction)
    00 = Level M (Medium - ~15%)
    11 = Level Q (Quartile - ~25%)
    10 = Level H (High - ~30%)
    """
    def __init__(self,bredde=25,rutebredde=15,error_correction=1,mask=5):
        self.bredde = bredde
        self.bitstream = None
        self.format_string = None
        self.error_correction = error_correction
        self.mask = mask
        self.final_mask = "101010000010010"
        self.rutebredde = rutebredde
        self.padx = 15
        self.pady = 15
        self.rs = reedsolo.RSCodec(8)
        self.grid = self.createGrid()
    
    def text_to_bits(self,text):
        text_bytes = list(text.encode("utf-8"))
        print(f"text as array: {text_bytes}")
        # Encode using Reed-Soloman error correction.
        encoded_text = self.rs.encode(text_bytes)
        print("R-S Encoded text:")
        print(list(encoded_text))
        # Konverter alle tall til en 8-bit stream:
        self.bitstream = []
        for tall in list(encoded_text):
            tall_byte = self.decimalToBinary(tall)
            self.bitstream.append(tall_byte)
        print(self.bitstream)
        

    def createGrid(self):
        grid = []
        n_ruter = self.bredde * self.rutebredde
        print(f"n_ruter = {n_ruter}")
        for j in range(self.bredde):
            y = j * self.rutebredde + self.pady
            grid.append([])
            for i in range(self.bredde):
                x = i * self.rutebredde + self.padx
                grid[j].append(Rute(i,j,x,y,self.rutebredde))
        return grid

    def drawGrid(self,canvas):
        for rad in self.grid:
            for rute in rad:
                #print(rute.id)
                rute.tegnRute(canvas)
    
    def drawDefaultCode(self,canvas):
        for rute in coordinates:
            j = rute[1]
            i = rute[0]
            rute = self.grid[j][i]
            rute.fill = "black"
            canvas.itemconfig(rute.rect, fill=rute.fill)
    
    def drawDataRedSquares(self,canvas):
        for rute in data_coordinates:
            j = rute[1]
            i = rute[0]
            rute = self.grid[j][i]
            rute.fill = "red"
            canvas.itemconfig(rute.rect, fill=rute.fill)

    def decimalToBinary(self,tall,n=8):
        output = ""
        while tall > 0:
            rest = tall % 2; # finner resten når vi deler på to: enten 1 eller 0.
            output += str(rest)
            tall = tall // 2 # heltallsdivisjon gjør at kun heltallet står igjen.
        # Legger til padding bits opp til 8 bits
        while len(output) < n:
            output += "0"
        # Algoritmen ender opp med å sette verdien av hver bit baklengs, starter med 1-er plassen.
        output = output[::-1]   # Reverserer tekststrengen ved å plukke ut substring baklengs.
        
        return output

    def create_format_string(self):
        ec_level = self.decimalToBinary(self.error_correction,2)
        mask_number = self.decimalToBinary(self.mask,3)
        self.format_string = ec_level + mask_number


    def XOR(self,tall1, tall2):
        """XOR av tall1 og tall2"""
        t1 = int(tall1,2)    # base 2
        t2 = int(tall2,2)    # base 2
        # Return the bits as string padded to 15 bits
        return f"{t1 ^ t2:15b}"
    
    def mask_format_string(self):
        mask = "10100110111"
        mask_padded = mask
        error_correction = self.format_string
        padding_len = 15-len(error_correction)
        padding = ""
        for i in range(padding_len):
            padding += "0"
        error_correction = error_correction + padding
        print(f"format string original: {error_correction}")
        # Remove leading zeros
        while error_correction[0] == "0":
            error_correction = error_correction[1:]
        print(f"format string no leading zeros: {error_correction}")
        while len(mask_padded) < len(error_correction):
            mask_padded += "0"
        print(f"Masking bits with padding: {mask_padded}, length: {len(mask_padded)}")
        # Aplly XOR mask in several steps until format_string is 10 bits or shorter.
        teller = 1
        while len(error_correction) >= 11:
            error_correction = self.XOR(error_correction,mask_padded)
            index = error_correction.index("1")
            error_correction = error_correction[index:]
            print(f"division {teller}: format-string masked: '{error_correction}', len: {len(error_correction)}")
            # For each time the format string returns it has a leading 0.
            # 1) Remove 0.
            # 2) Remove trailing 0 from masking string.
            teller += 1
            # Remove any leading 0 from bitstream:
            if error_correction[0] == "0":
                error_correction = error_correction[1:]
            # Pad the masking polynomial to length of format_string:
            mask_padded = mask
            while len(mask_padded) < len(error_correction):
                mask_padded += "0"
            if teller >= 10:
                print("Aborts!")
                return True
        # Combine original format_string with error correction.
        self.format_string += error_correction
        # XOR final format string with this mask: 101010000010010
        self.format_string = self.XOR(self.format_string,self.final_mask)
        return self.format_string

    def draw_format_string(self,canvas):
        # Draw upper left format string
        teller = 0
        for rute in formatting_data_upper_left:
            j = rute[1]
            i = rute[0]
            rute = self.grid[j][i]
            if self.format_string[teller] == "1":
                rute.fill = "black"
            else:
                rute.fill = "white"
            canvas.itemconfig(rute.rect, fill=rute.fill)
            teller += 1
        
        # Draw right formatting
        teller = 0
        for rute in formatting_data_right:
            j = rute[1]
            i = rute[0]
            rute = self.grid[j][i]
            if self.format_string[teller] == "1":
                rute.fill = "black"
            else:
                rute.fill = "white"
            rute.fill = "dodgerblue"
            canvas.itemconfig(rute.rect, fill=rute.fill)
            teller += 1