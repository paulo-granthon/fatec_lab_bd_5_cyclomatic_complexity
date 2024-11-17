def example_function2(y):
    """
    Performs different operations based on the value of y:
    - Continuously reduces y while printing the result.
    - If y is odd, decrease by 1; if even, divide by 2.

    Args:
    y (int): The number to manipulate.

    Returns:
    None
    """
    while y > 0:
        if y % 2 == 1:
            y -= 1
        else:
            y //= 2
        print(y)
