"""Lag et program som bruker Pythagoras for å beregne den lengste siden (hypotenusen) i 
en rettvinklet trekant. 
(Husk at c2 = a2 + b2, der c er den lengste siden i trekanten.)"""

import math

# Perfekt rettvinklet: 3, 4, 5
a = 3
b = 4

c = math.sqrt(a**2 + b**2)

print(c)