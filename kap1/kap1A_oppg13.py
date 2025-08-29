""" Du skal nå bruke biblioteket «calendar» til å skrive ut en kalender for 
måneden vi er i. For å lage en slik kalender kan vi bruke funksjonen month() 
som finnes i biblioteket. I parentesen skriver vi årstall og månedsnummer, 
for eksempel month(2014, 6), som gir måneden juni i 2014. For å se 
kalenderen må vi skrive den ut med print(). Du kan også skrive ut måneden 
og årstallet da du ble født. Hvilken ukedag ble du født på?
"""

import calendar

hm = calendar.month(1983,5) # Henrik

k = calendar.month(1997,4) # Kristine
al = calendar.month(2017,5) # Amanda Lorenthine
va = calendar.month(2024,2) # Victor August




print(hm)
print(k)
print(al)
print(va)