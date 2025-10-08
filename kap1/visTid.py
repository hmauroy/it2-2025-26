"""Printer ut tiden.
Eksempel: 1 759 731 863.328247
Dokumentasjon:
https://www.w3schools.com/python/python_datetime.asp
"""
from time import time
import datetime

def visTid():
    tid = time()
    print(tid)

def visTidForbedret():
    """Printer ut tiden sånn at mennesker kan lese den.
    Dato, klokkeslett: 2025-10-06 08:28:00.156811
    """
    x = datetime.datetime.now()
    print(x.strftime("%d.%m.%Y kl. %H:%M"))



visTidForbedret()