def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out

result1 = flip_case('Aaaahhh', 'a')
print(result1)  # Output: 'aAAAhhh'

result2 = flip_case('Aaaahhh', 'A')
print(result2)  # Output: 'aAAAhhh'

result3 = flip_case('Aaaahhh', 'h')
print(result3)  # Output: 'AaaaHHH'

