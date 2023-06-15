def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    return lst[::2]

lst = [1, 2, 3, 4, 5]
result = remove_every_other(lst)
print(result)  # Output: [1, 3, 5]

print(lst)  # Output: [1, 2, 3, 4, 5]
