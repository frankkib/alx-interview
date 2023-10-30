#!/usr/bin/python3
"""
Prime interview question
"""


def is_prime(num):
    """
    Function  for checking if the number is prime or not
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    function for finding the winner
    """
    if x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
