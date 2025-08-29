"""I «math»-biblioteket finner vi funksjoner for sinus (sin()), cosinus (cos()) 
og tangens (tan()). Du husker kanskje at cos space alpha equals fraction 
numerator hosliggende space katet over denominator hypotenus end fraction? 
Kan du finne den ukjente siden x i figuren? Vinkelen er oppgitt i grader, 
men i «math»-biblioteket brukes radianer. Du må derfor først finne ut 
hvordan du kan gjøre om vinkelen til radianer.
Trekant ABC har sidene a, b, c
a = 7
b = blank
c = x
vinkel beta (motstående for b) = 60 deg

cos u = hos/hyp

cos 60 = 7/x

x = 7 / cos 60
"""
import math

a = 7
v = 60
# Gjør om til radianer
v_radianer = v * math.pi/180

x = a / (math.cos(v_radianer))
print(f"x = {x:.15f}")

