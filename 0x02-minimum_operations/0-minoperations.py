def minOperations(n):
    """
    Calculate the minimum number of operations needed
    to get exactly n 'H' characters in a text file.

    Operations allowed:
    - Copy All
    - Paste

    Parameters:
    n (int): The target number of 'H' characters

    Returns:
    int: The fewest number of operations needed to
    achieve exactly n 'H' characters
    If n is impossible to achieve, return 0
    """

    if n <= 1:
        return 0

    operations = 0  # Initialize the total number of operations
    factor = 2  # Start with the smallest prime factor

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
