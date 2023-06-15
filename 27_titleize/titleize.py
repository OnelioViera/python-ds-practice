def titleize(phrase):
    """Return phrase in title case (each word capitalized).

    >>> titleize('this is awesome')
    'This Is Awesome'

    >>> titleize('oNLy cAPITALIZe fIRSt')
    'Only Capitalize First'
    """
    # there's a built-in method for this!
    return phrase.title()


print(titleize("this is awesome"))  # Output: 'This Is Awesome'
print(titleize("oNLy cAPITALIZe fIRSt"))  # Output: 'Only Capitalize First'
