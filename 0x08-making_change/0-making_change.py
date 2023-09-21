#!/usr/bin/python3
"""
Module for number of coins needed
"""


def makeChange(coins, total):
    """
    Function for finding the minimum coins
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    return dp[total]
