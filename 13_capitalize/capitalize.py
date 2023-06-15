def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    return phrase.capitalize()
    
result1 = capitalize('python')
print(result1)  # Output: 'Python'

result2 = capitalize('only first word')
print(result2)  # Output: 'Only first word'
