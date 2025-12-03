"""
Sum med imperativ kode (lesbart og forståelig).
"""

def sum_liste(tall):
    total = 0
    for t in tall:
        total += t
    return total

print(sum_liste([1,2,3,4,5,6,7,8,9]))

