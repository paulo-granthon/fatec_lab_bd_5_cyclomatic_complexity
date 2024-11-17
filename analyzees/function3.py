def example_function3(z):
    """
    Returns a string based on the value of z:
    - "Big number" if z > 100.
    - "Exactly 100" if z is 100.
    - "Small number" if z is less than 100.

    Args:
    z (int): The number to categorize.

    Returns:
    str: A description based on the value of z.
    """
    if z > 100:  # Cyclomatic complexity +1
        return "Big number"
    if z == 100:  # Cyclomatic complexity +1
        return "Exactly 100"
    return "Small number"

# Total Cyclomatic Complexity: 3
