"""
Lag lista verdensdeler som inneholder verdensdelenes navn. 
Skriv ut den første, midterste og siste verdensdelen i lista. 
Bruk både positive og negative indekser for å skrive ut verdiene.
"""
verdensdeler = ["Afrika","Asia","Antarktis","Europa","Nord-Amerika, Sør-Amerika","Oseania"]
verdensdeler_folketall = [1.46,4.77,0,0.72,0.59,0.43,0.045]

for i in range(len(verdensdeler)):
    print(verdensdeler[i], end=": ")
    print(verdensdeler_folketall[i])
print(verdensdeler[0])
print(verdensdeler[len(verdensdeler)//2])
print(verdensdeler[-1])
