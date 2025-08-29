"""
Dragonslayer
Regler
1) Hvis du trekker tilfeldig 0 eller 1 får du angripe dragen.
2) Hvis du angriper skal skaden på dragen øke med tilfeldig tall fra og med 1 og til og med 5.
3) Hvis total skade er større eller lik 4 vinner du.
4) Hvis dragen angriper deg har du tapt.
"""
from random import random
import math

slaying = True
you_hitting = math.floor(random() * 2)
total_damage = 0

while(slaying):
    damage_this_round = math.floor(random() * 5 + 1)
    if you_hitting == 1:
        print("You're punishing the dragon!")
        print(damage_this_round)
        total_damage = total_damage + damage_this_round
        if total_damage >= 4:
            print(f"The dragon is defeated at {total_damage} damage.")
            slaying = False
        else:
            you_hitting = math.floor(random() * 2)
    else:
        print("The dragon defeated you!")
        slaying = False

        