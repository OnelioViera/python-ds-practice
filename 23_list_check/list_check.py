def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for item in lst:
        if not isinstance(item, list):
            return False

    return True

result1 = list_check([[1], [2, 3]])
print(result1)  # Output: True

result2 = list_check([[1], "nope"])
print(result2)  # Output: False
