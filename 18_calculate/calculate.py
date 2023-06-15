def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    if operation == "add":
        res = a + b
    elif operation == "subtract":
        res = a - b
    elif operation == "multiply":
        res = a * b
    elif operation == "divide":
        res = a / b
    else:
        return

    if make_int:
        res = int(res)

    return f"{message} {res}"

result1 = calculate('add', 2.5, 4)
print(result1)  # Output: 'The result is 6.5'

result2 = calculate('subtract', 4, 1.5, make_int=True)
print(result2)  # Output: 'The result is 2'

result3 = calculate('multiply', 1.5, 2)
print(result3)  # Output: 'The result is 3.0'

result4 = calculate('divide', 10, 4, message='I got')
print(result4)  # Output: 'I got 2.5'

result5 = calculate('foo', 2, 3)
print(result5)  # Output: None

