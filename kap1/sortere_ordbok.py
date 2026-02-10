"""
Spørsmål til Claude 4.5 Sonnet 29.10.2025.

Q: Hi. How do I sort a dictionary by values in python?

"""

my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

# Returns a list of tuples sorted by value
sorted_items = sorted(my_dict.items(), key=lambda x: x[1])
# Result: [('banana', 1), ('cherry', 2), ('apple', 3)]

# Convert back to dictionary (Python 3.7+ maintains insertion order)
sorted_dict = dict(sorted_items)