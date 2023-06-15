def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    counter = {}
    for letter in phrase:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

result1 = multiple_letter_count('yay')
print(result1)  # Output: {'y': 2, 'a': 1}

result2 = multiple_letter_count('Yay')
print(result2)  # Output: {'Y': 1, 'a': 1, 'y': 1}
