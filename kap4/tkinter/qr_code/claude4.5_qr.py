import qrcodegen
from PIL import Image

# Define the error correction level and version for the QR code
error_correction = qrcodegen.QrCode.Ecc.LOW  # Equivalent to ERROR_CORRECT_L
version = 2

# Function to convert text to binary
def convert_to_8bit(data):
    return ''.join(format(ord(char), '08b') for char in data)

# Generate QR code from encoded text data WITHOUT masking
def generate_qr_code(text, mode="utf-8"):
    # Create segments manually to control version
    segments = qrcodegen.QrSegment.make_segments(text)
    
    # Force version 2 by specifying minversion and maxversion
    qr = qrcodegen.QrCode.encode_segments(
        segments, 
        error_correction,
        minversion=version,
        maxversion=version,
        mask=-1,  # Auto-select best mask
        boostecl=False
    )
    
    # Get the size of the QR code
    size = qr.get_size()
    
    print(f"QR Code Version: {qr._version}")
    print(f"QR Code Size: {size}x{size}")
    print(f"Mask Pattern Used: {qr._mask}")
    
    # Get the UNMASKED modules matrix
    print("\nModules Matrix (without final masking):")
    unmasked_modules = []
    for y in range(size):
        row = []
        for x in range(size):
            # Get module - qrcodegen returns the MASKED version by default
            is_dark = qr.get_module(x, y)
            
            # Get the mask pattern value at this position
            mask_value = get_mask_pattern(qr._mask, x, y)
            
            # XOR to reverse the mask (only for data/EC regions)
            if is_function_module(qr, x, y):
                # Function modules (finder patterns, timing, etc.) are never masked
                unmasked = is_dark
            else:
                # Data/EC modules: reverse the mask
                unmasked = is_dark ^ mask_value
            
            row.append(unmasked)
        unmasked_modules.append(row)
        print([1 if cell else 0 for cell in row])  # Print as 1s and 0s for clarity
    
    # Read out the data bits in QR code order
    print("\n" + "="*60)
    print("READING DATA FROM QR CODE")
    print("="*60)
    data_bits = read_data_bits(unmasked_modules, qr._version, size)
    
    # Convert bits to codewords (8-bit chunks)
    print("\nData stream as binary:")
    print(data_bits)
    print(f"\nTotal bits read: {len(data_bits)}")
    
    codewords = []
    print("\nCodewords (8-bit chunks):")
    for i in range(0, len(data_bits), 8):
        byte_str = data_bits[i:i+8]
        if len(byte_str) == 8:
            decimal_value = int(byte_str, 2)
            codewords.append(decimal_value)
            print(f"Codeword {len(codewords):2d}: {byte_str} = {decimal_value:3d} (0x{decimal_value:02X})")
    
    print(f"\nTotal codewords: {len(codewords)}")
    print(f"Codewords as decimal list: {codewords}")
    
    # Convert the encoded text to binary
    encoded_text = convert_to_8bit(text)
    
    # Create image from UNMASKED modules
    scale = 10  # box_size equivalent
    border = 4
    img_size = (size + border * 2) * scale
    img = Image.new('1', (img_size, img_size), 1)  # 1-bit image, white background
    
    pixels = img.load()
    for y in range(size):
        for x in range(size):
            if unmasked_modules[y][x]:
                # Draw black box
                for dy in range(scale):
                    for dx in range(scale):
                        px = (x + border) * scale + dx
                        py = (y + border) * scale + dy
                        pixels[px, py] = 0
    
    # Save the image
    if mode == "utf-8":
        text_mode = "text"
        version_error_correction = 1
    elif mode == "ascii":
        text_mode = "ascii"
        version_error_correction = 3
    else:
        raise ValueError("Unsupported encoding mode")
    
    img.save(f"qr_code_{text_mode}_{version_error_correction}_unmasked.png", "PNG")
    
    # Also create a MASKED version for comparison
    img_masked = Image.new('1', (img_size, img_size), 1)
    pixels_masked = img_masked.load()
    for y in range(size):
        for x in range(size):
            if qr.get_module(x, y):
                for dy in range(scale):
                    for dx in range(scale):
                        px = (x + border) * scale + dx
                        py = (y + border) * scale + dy
                        pixels_masked[px, py] = 0
    img_masked.save(f"qr_code_{text_mode}_{version_error_correction}_masked.png", "PNG")
    
    return encoded_text, img, codewords

# Function to read data bits from unmasked QR code matrix
def read_data_bits(modules, version, size):
    """
    Read data bits from QR code in the correct order.
    QR codes are read from bottom-right, going upward in 2-column strips.
    """
    bits = []
    
    # Start from rightmost column, move left in pairs
    # Skip column 6 (vertical timing pattern)
    x = size - 1
    direction = -1  # -1 = going up, +1 = going down
    
    while x > 0:
        # Skip timing column
        if x == 6:
            x -= 1
        
        # Process two columns at a time (right column first, then left)
        for y_range in range(size):
            if direction == -1:  # Going up
                y = size - 1 - y_range
            else:  # Going down
                y = y_range
            
            # Read right column of the pair first, then left column
            for dx in [0, -1]:
                curr_x = x + dx
                curr_y = y
                
                # Skip function modules
                if not is_function_module_for_reading(version, curr_x, curr_y, size):
                    bit = '1' if modules[curr_y][curr_x] else '0'
                    bits.append(bit)
        
        # Switch direction for next pair of columns
        direction *= -1
        x -= 2
    
    return ''.join(bits)

def is_function_module_for_reading(version, x, y, size):
    """Check if a module is a function module (should be skipped when reading data)"""
    # Finder patterns (top-left, top-right, bottom-left) + separators
    if (x < 9 and y < 9) or (x >= size - 8 and y < 9) or (x < 9 and y >= size - 8):
        return True
    
    # Timing patterns (row 6 and column 6)
    if x == 6 or y == 6:
        return True
    
    # Dark module (at position (8, 4*version + 9))
    if x == 8 and y == 4 * version + 9:
        return True
    
    # Alignment patterns for version 2
    if version == 2:
        align_pos = 18
        if abs(x - align_pos) <= 2 and abs(y - align_pos) <= 2:
            return True
    
    # Format information (around finder patterns)
    # Horizontal format info (top)
    if y == 8 and (x < 9 or x >= size - 8):
        return True
    # Vertical format info (left)
    if x == 8 and (y < 9 or y >= size - 7):
        return True
    
    return False

# Helper function to calculate mask pattern value at position (x, y)
def get_mask_pattern(mask_num, x, y):
    """Returns True if the mask pattern is dark at position (x, y)"""
    if mask_num == 0:
        return (x + y) % 2 == 0
    elif mask_num == 1:
        return y % 2 == 0
    elif mask_num == 2:
        return x % 3 == 0
    elif mask_num == 3:
        return (x + y) % 3 == 0
    elif mask_num == 4:
        return (x // 3 + y // 2) % 2 == 0
    elif mask_num == 5:
        return (x * y) % 2 + (x * y) % 3 == 0
    elif mask_num == 6:
        return ((x * y) % 2 + (x * y) % 3) % 2 == 0
    elif mask_num == 7:
        return ((x + y) % 2 + (x * y) % 3) % 2 == 0
    else:
        raise ValueError("Invalid mask pattern")

# Helper function to check if a module is a function module (never masked)
def is_function_module(qr, x, y):
    """Check if module at (x, y) is a function module (finder, timing, etc.)"""
    size = qr.get_size()
    
    # Finder patterns (top-left, top-right, bottom-left) + separators
    if (x < 9 and y < 9) or (x >= size - 8 and y < 9) or (x < 9 and y >= size - 8):
        return True
    
    # Timing patterns (horizontal and vertical lines at row 6 and column 6)
    if x == 6 or y == 6:
        return True
    
    # Dark module (always at position (8, 4*version + 9))
    if x == 8 and y == 4 * qr._version + 9:
        return True
    
    # Alignment patterns (for version 2 and higher)
    if qr._version >= 2:
        # Version 2 has alignment pattern at (18, 18)
        if qr._version == 2:
            align_pos = 18
            if abs(x - align_pos) <= 2 and abs(y - align_pos) <= 2:
                return True
    
    # Format information (around finder patterns)
    # Horizontal format info (top)
    if y == 8 and (x < 9 or x >= size - 8):
        return True
    # Vertical format info (left)
    if x == 8 and (y < 9 or y >= size - 7):
        return True
    
    return False

# Example usage
text_data = "HEI IT2!"
encoded_text, img, codewords = generate_qr_code(text_data)

print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"Original text: {text_data}")
print(f"Encoded Text (binary): {encoded_text}")
print(f"Extracted codewords: {codewords}")
print("\nTwo images saved:")
print("- Unmasked version (raw data)")
print("- Masked version (scannable)")
img.show()