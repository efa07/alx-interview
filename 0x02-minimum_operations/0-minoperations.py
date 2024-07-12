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

    next = 'H'
    body = 'H'
    operations = 0
    while (len(body) < n):
        if n % len(body) == 0:
            operations += 2
            next = body
            body += body
        else:
            operations += 1
            body += next
    if len(body) != n:
        return 0
    return operations
