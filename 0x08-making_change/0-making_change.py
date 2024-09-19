#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
    coins (List[int]): A list of integers representing the values of
    available coins.
    total (int): The total amount of money to make using the fewest coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
         Returns 0 if the total is 0 or less.
         Returns -1 if the total cannot be made using the given coins.
    Approach:
    - Use dynamic programming to build up the solution for each total from
      0 to the target total.
      - Create an array `dp` where `dp[i]` represents the minimum number of
    coins needed to make total `i`.
    - Initialize `dp[0] = 0` (no coins needed to make a total of 0).
    - For each coin, update the dp array to ensure the fewest coins are
      selected for each total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
