def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    
    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)

    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst

lst = [1, 2, 3]

result1 = list_manipulation(lst, 'remove', 'end')
print(result1)  # Output: 3

result2 = list_manipulation(lst, 'remove', 'beginning')
print(result2)  # Output: 1

print(lst)  # Output: [2]

result3 = list_manipulation(lst, 'add', 'beginning', 20)
print(result3)  # Output: [20, 2]

result4 = list_manipulation(lst, 'add', 'end', 30)
print(result4)  # Output: [20, 2, 30]

print(lst)  # Output: [20, 2, 30]

result5 = list_manipulation(lst, 'foo', 'end')
print(result5 is None)  # Output: True

result6 = list_manipulation(lst, 'add', 'dunno')
print(result6 is None)  # Output: True
