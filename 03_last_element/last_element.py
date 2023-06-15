def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    
    if lst:
        return lst[-1]
    
result1 = last_element([1, 2, 3])
print(result1)  # Output: 3

result2 = last_element([])
print(result2 is None)  # Output: True
