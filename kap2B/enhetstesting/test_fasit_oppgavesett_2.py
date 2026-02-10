"""

Test-suite for diverse funksjoner.
Elevene skal implementere funksjonene slik at alle testene består.


"""

def absolute_value(number):
    if number < 0:
        return -number
    return number


def count_characters(text):
    return len(text)


def is_divisible(a, b):
    return a % b == 0


def max_of_three(a, b, c):
    return max(a, b, c)


def sum_even_numbers(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total


def reverse_string(text):
    return text[::-1]


def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


def count_positive_numbers(numbers):
    count = 0
    for n in numbers:
        if n > 0:
            count += 1
    return count


def is_palindrome(text):
    return text == text[::-1]


def unique_elements(numbers):
    result = []
    for n in numbers:
        if n not in result:
            result.append(n)
    return result


def test_absolute_value():
    assert absolute_value(5) == 5
    assert absolute_value(-3) == 3
    assert absolute_value(0) == 0


def test_count_characters():
    assert count_characters("hei") == 3
    assert count_characters("") == 0
    assert count_characters("Python") == 6


def test_is_divisible():
    assert is_divisible(10, 5) == True
    assert is_divisible(10, 3) == False
    assert is_divisible(0, 1) == True


def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(9, 3, 6) == 9
    assert max_of_three(-1, -5, -3) == -1


def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4]) == 6
    assert sum_even_numbers([]) == 0
    assert sum_even_numbers([2, 4, 6]) == 12


# Høyt nivå (6–10)

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("radar") == "radar"


def test_remove_vowels():
    assert remove_vowels("hei") == "h"
    assert remove_vowels("python") == "pythn"
    assert remove_vowels("AEIOU") == ""


def test_count_positive_numbers():
    assert count_positive_numbers([1, -2, 3, 0, 5]) == 3
    assert count_positive_numbers([]) == 0
    assert count_positive_numbers([-1, -2, -3]) == 0


def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("python") == False
    assert is_palindrome("level") == True


def test_unique_elements():
    assert unique_elements([1, 2, 2, 3]) == [1, 2, 3]
    assert unique_elements([]) == []
    assert unique_elements([5, 5, 5]) == [5]