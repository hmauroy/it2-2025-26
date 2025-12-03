"""
Returnerer binære tallsekvenser som koder L, G og R barcode segmenter.

Avhengig av første siffer hvilken kode som skal letes opp:
First digit	First group of 6 digits	Last group of 6 digits
0	LLLLLL	RRRRRR
1	LLGLGG	RRRRRR
2	LLGGLG	RRRRRR
3	LLGGGL	RRRRRR
4	LGLLGG	RRRRRR
5	LGGLLG	RRRRRR
6	LGGGLL	RRRRRR
7	LGLGLG	RRRRRR
8	LGLGGL	RRRRRR
9	LGGLGL	RRRRRR

"""
from digits_encodings import digits_table, LG_sequences


def generateBarcode(numbers_string):
    """
    1) Put into output list start marker binary code: 101
    2) Get LG-sequence from the first digit.
    3) For the next 6 digits get their binary code from the LG-sequence. Put binary LG code into left output list.
    4) Put in the center marker binary code: 01010 
    5) For the last 5 digits get binary codes from R-sequence. Put binary R code into output list.
    6) Calculate the checksum for the last digit.
    7) Put in the end marker binary code: 101
    """
    startEnd_code = [1,0,1]
    center_code = [0,1,0,1,0]
    digits = [int(char) for char in numbers_string]
    output = [*startEnd_code]
    # 2)
    sequence = get_LG_sequence(digits[0])
    # 3)
    for i in range(6):
        letter = sequence[i]
        digit = digits[i+1]
        binary_code = digits_table[digit][letter]
        output += binary_code
        print(f"{digit}{letter}: {binary_code}")
    print("")
    # 4)
    output += center_code
    # 5) R sequence for the right side.
    for j in range(7,7+5):
        digit = digits[j]
        binary_code = digits_table[digit]['R']
        output += binary_code
        print(f"{digit}{'R'}: {binary_code}")
    # 6)
    check = calc_checksum(numbers_string)
    binary_code = digits_table[check]['R']
    output += binary_code
    print(f"{check}{'R'}: {binary_code}")
    # 7)
    output += startEnd_code
    return output, check


def get_LG_sequence(firstDigit):
    """Returns the sequence of L and G for a certain starting digit."""
    return LG_sequences[firstDigit]


def calc_checksum(number):
    """
    Checksum-algoritme
1. Summer oddetallsplassene
2. Gang med 3
3. Legg til sum partallsplassene
4. Checksum = Sum % 10
5. Hvis 0 er det null
    Ellers 10 - checksum
    """
    print("Checksum calculation")
    lst1 = list(str(number))
    if len(lst1) == 13:
        print("13 digit number!")
        lst1.pop()
        #print(lst1)
    sum = 0
    for i in range(1,len(lst1),2):
        sum += int(lst1[i])
    sum = sum * 3
    for i in range(0,len(lst1),2):
        sum += int(lst1[i])
    checksum = sum % 10
    if checksum != 0:
        return 10 - checksum
    else:
        return 0

if __name__ == "__main__":

    generateBarcode("1234567890128")
    exit()
    print(calc_checksum("1234567890128"[:-1]))
    print(calc_checksum("4003994155486"[:-1]))
    print(calc_checksum("8711253001202"[:-1]))

