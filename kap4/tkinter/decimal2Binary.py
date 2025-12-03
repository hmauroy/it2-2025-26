"""
Fra titallssystemet til totallssystemet.
"""

def decimalToBinary(tall):
    output = ""
    while tall > 0:
        rest = tall % 2; # finner resten når vi deler på to: enten 1 eller 0.
        output += str(rest)
        tall = tall // 2 # heltallsdivisjon gjør at kun heltallet står igjen.
    # Algoritmen ender opp med å sette verdien av hver bit baklengs, starter med 1-er plassen.
    output = output[::-1]   # Reverserer tekststrengen ved å plukke ut substring baklengs.
    """
    # Ønsker du å gjøre det med for-løkke så kan det gjøres slik:
    reversert = ""
    for i in range(len(output)-1,-1,-1): # Går baklengs gjennom listen
        reversert += output[i]
    output = reversert
    """ 
    return output


def decimalToBinaryBad(tall):
    rest = tall
    output = ""
    grad = 0
    while tall // 2**grad != 0:
        grad += 1
        if grad >= 100:
            print("Noe gikk galt.")
            break
    #print(f"Høyeste bit: {grad}")
    for i in range(grad-1,-1,-1):
        #print(f"i: {i}: {tall} % {2**i} = {tall-2**i} neste tall: {tall-2**i}")
        if tall - 2**i >= 0:
            output += "1"
            tall = tall - 2**i
        elif tall == 1 and i == 0:
            output += "1"
        else:
            output += "0"
    return output

def test_algoritmene_mot_hverandre():
    for i in range(100):
        print(decimalToBinaryBad(i) == decimalToBinary(i), i, decimalToBinaryBad(i),decimalToBinary(i))

if __name__ == "__main__":
    binært = decimalToBinaryBad(255)
    print(binært)
    print(f"{len(binært)}-bit")
