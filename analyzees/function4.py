def example_function4(n):
    """
    Calculates the factorial of a number recursively.
    If the input number is less than or equal to 1, it returns 1.
    Otherwise, it recursively multiplies the number by the factorial of the
    previous number.

    Args:
    n (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number.
    """
    if n <= 1:  # Cyclomatic complexity +1
        return 1

    return n * example_function4(n - 1)

# Total Cyclomatic Complexity: 2
