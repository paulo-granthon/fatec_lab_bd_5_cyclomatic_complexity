def example_function5(a, b):
    """
    Checks if a pair of numbers are both positive or both negative, and returns
    a corresponding message. If neither condition is met, it returns 'Mixed
    signs'.

    Args:
    a (int): The first number.
    b (int): The second number.

    Returns:
    str: A message indicating the relationship between the two numbers.
    """
    if a > 0 and b > 0:
        return "Both numbers are positive"
    if a < 0 and b < 0:
        return "Both numbers are negative"

    return "Mixed signs"
