first = "10101110"
second = "10010010"
f = int(first,2)    # base 2
s = int(second,2)
hex1 = int("ff",16) # base 16

print(f'first  :{f:08b}')
print(f'second :{s:08b}')

#08b betyr LEDENDE 0 og 8 tegn
print(f'AND    :{f & s:08b}') # 1 hvis begge bits er 1
print(f'OR     :{f | s:08b}') # 1 hvis én av bits er 1
print(f'XOR    :{f ^ s:08b}') # XOR på to korresponderende bits gir 1 hvis bits er forskjellige.
print(f'OCOMP  :{~f & 255:08b}') # ones kompliment må bruke mask med 11111111 = 255 for å få riktig tall ut.
print(f'SHIFTL :{f<<2 & 255:08b}') # Shift left må ta maske med 255 for å fjerne leading plasser. Masken settes på til høyre!
print(f'SHIFTR :{f>>2:08b}') # Trenger ikke bit-maske med 255.


skiftet = f<<2
print(f"10101110 << 2 = {skiftet:010b}")
and1 = skiftet & 255
print(f"10101110 << 2 = {and1:010b}")
print(f'0e i hex = {int("0e",16)}')

tall1 = "011010000000000"
tall2 = "101010000010010"
t1 = int(tall1,2)    # base 2
t2 = int(tall2,2)    # base 2
print(f"{t1 ^ t2:15b}")