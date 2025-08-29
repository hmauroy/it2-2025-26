from random import randint

is_playing = True
total_damage = 0

while is_playing:
    terning = randint(0,1)
    """
    Regler
    1) Hvis du trekker fra tallene 0 og 1 verdien 1 får du angripe dragen 
    2) Hvis du angriper skal skaden på dragen øke med tilfeldig tall fra og med 1 og til og med 5.
    3) Hvis total skade er større eller lik 4 vinner du.
    4) Hvis dragen angriper deg har du tapt.
    """