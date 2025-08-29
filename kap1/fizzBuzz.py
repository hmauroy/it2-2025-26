"""
Skriv ut tallene fra og med 0 til og med 100. 
Hvis tallet er delelig på 3 skrives det ikke ut tallet, 
men ordet 'Fizz'. 
Hvis det er delelig på 5, skrives det ut 'Buzz'. 
Hvis det er delelig på både 3 og 5 skrives det ut 'FizzBuzz'.
Utfordring: Bruk så få linjer med kode som mulig :)
"""
tekst = ""
for i in range(0,101):
    if i % 3 == 0:
      tekst = "Fizz"
    
    if i % 5 == 0:
       tekst = tekst + "Buzz"
    
    if tekst == "":
       tekst = i

    print(tekst)
    tekst = ""


