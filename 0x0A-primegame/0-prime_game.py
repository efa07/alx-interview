#!/usr/bin/python3
"""Module for Prime Game"""

def isWinner(x, nums):
    """
    This module contains the implementation of the prime game.
    The prime game is played between two players, Maria and Ben.
      The game is played in rounds, and in each round, a number
        n is chosen. The players take turns picking prime numbers
          from the set {1, 2, ..., n}. The player who cannot pick a
          prime number loses the round. The winner of the game is the
          player who wins the most rounds.
    Functions:
        isWinner(x, nums): Determines the winner of the prime game
        after x rounds.
        Args:
            x (int): The number of rounds to be played.
            nums (list of int): A list of integers representing the
            upper limit of the set for each round.
        Returns:
            str: The name of the player who won the most rounds
              ("Maria" or "Ben"). If there is a tie, returns None.
    """
    # Step 1: Sieve of Eratosthenes to find all primes up to 10000
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for start in range(2, int(max_n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_n + 1, start):
                is_prime[multiple] = False

    # Step 2: Count the number of primes up to each n
    prime_counts = [0] * (max_n + 1)
    for num in range(1, max_n + 1):
        prime_counts[num] = prime_counts[num - 1] + (1 if is_prime[num] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:  # Odd number of primes
            maria_wins += 1
        else:  # Even number of primes
            ben_wins += 1

    # Step 4: Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
