def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    return word.lower().count(letter.lower())

result1 = single_letter_count('Hello World', 'h')
print(result1)  # Output: 1

result2 = single_letter_count('Hello World', 'z')
print(result2)  # Output: 0

result3 = single_letter_count("Hello World", 'l')
print(result3)  # Output: 3
