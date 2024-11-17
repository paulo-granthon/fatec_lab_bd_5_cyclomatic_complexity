def example_function1(x):
    """
    Returns a string based on the value of x:
    - "Even" if x is a positive even number.
    - "Odd" if x is a positive odd number.
    - "Negative Even" if x is a negative even number.
    - "Negative Odd" if x is a negative odd number.
    - A range of integers from 0 to x (exclusive) if x is

    Args:
    x (int): The number to categorize.

    Returns:
    str: A description of the number's parity or a range of integers.
    """
    if x > 0:  # Cyclomatic complexity +1
        if x % 2 == 0:  # Cyclomatic complexity +1
            return "Even"
        return "Odd"
    for i in range(abs(x)):  # Cyclomatic complexity +1
        print(i)
    if x % 2 == 0:  # Cyclomatic complexity +1
        return "Negative Even"
    return "Negative Odd"

# Total Cyclomatic Complexity: 5
