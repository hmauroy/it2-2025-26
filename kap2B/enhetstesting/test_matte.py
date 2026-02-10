"""
En enkel enhetstest med pytest.

Kjøres ved å skrive i terminalen (stående i mappen):
pytest

"""
import math

# oppg 1
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

# oppg 2
def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(0,5) == 0
    assert multiply(-1,4) == -4

# oppg 3
def is_even(number):
    return number % 2 == 0


def test_is_even_manual():
    if is_even(2) != True:
        print("Feil på 2")
    if is_even(3) != False:
        print("Feil på 3")

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False

test_is_even_manual()

# oppg 4
def grade(score):
    if score >= 50:
        return "Bestått"
    return "Ikke bestått"

def test_grade():
    assert grade(50) == "Bestått"
    assert grade(49) == "Ikke bestått"

def test_grade_manuell():
    if grade(50) != "Bestått":
        print("Feil på grade(50)")
    if grade(49) != "Ikke bestått":
        print("Feil på grade(49)")

test_grade_manuell()

# Oppg 5
def double(x):
    return 2 * x

def test_double():
    assert double(2) == 4
    assert double(0) == 0
    assert double(-3) == -6

# oppg 6
def is_positive(x):
    if x > 0:
        return True
    else:
        return False

def test_is_positive():
    assert is_positive(5) == True
    assert is_positive(1) == True
    assert is_positive(0) == False
    assert is_positive(-3) == False


# oppg 7
def capitalize_word(mitt_ord):
    str1 = mitt_ord[0].upper()
    str1 += mitt_ord[1:]
    return str1


def test_capitalize_word():
    assert capitalize_word("python") == "Python"
    assert capitalize_word("kode") == "Kode"

# oppg 8
def sum_list(liste):
    return sum(liste)

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
    assert sum_list([5]) == 5


# oppg 9
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def test_fahrenheit_to_celsius():
    assert f"{fahrenheit_to_celsius(0):.3f}" == "-17.778"
    assert fahrenheit_to_celsius(50) == 10
    assert math.ceil(fahrenheit_to_celsius(98.5)) == 37
    assert int(fahrenheit_to_celsius(114)) == 45

# oppg 10
def kule_volum(radius):
    """Beregner volumet av en kule."""
    return (4/3) * math.pi * radius ** 3

def test_kule_volum():
    """-4.1887902047863905
    9202.7720799157
    129.87878804533656"""
    assert f"{kule_volum(10):.5f}" == "4188.79020"
    assert f"{kule_volum(math.pi):.5f}" == "129.87879"
    assert math.ceil(kule_volum(math.pi)) == 130
