"""
Rekursiv måte å beregne sum av en liste med tall.
"""

def sum_liste(tall):
    if tall:
        return tall[0] + sum_liste(tall[1:])
    else:
        return 0

print(sum_liste([1,2,3,4,5,6,7,8,9]))