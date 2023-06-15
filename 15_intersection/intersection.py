def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    set2 = set(l2)

    return [val for val in l1 if val in set2]

result1 = intersection([1, 2, 3], [2, 3, 4])
print(result1)  # Output: [2, 3]

result2 = intersection([1, 2, 3], [1, 2, 3, 4])
print(result2)  # Output: [1, 2, 3]

result3 = intersection([1, 2, 3], [3, 4])
print(result3)  # Output: [3]

result4 = intersection([1, 2, 3], [4, 5, 6])
print(result4)  # Output: []
