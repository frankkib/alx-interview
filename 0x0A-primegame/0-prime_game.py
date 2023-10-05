#!/usr/bin/python3
"""
The prime game interview question
"""


def isWinner(x, nums):
    """
    function that returns the prime winner
    """
    def isPrime(num):
        """
        function that checks for prime numbers
        """
        if num < 2:
            return False

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    dp = [None] * (max(nums) + 1)

    for n in range(2, (max(nums) + 1)):
        if dp[n] is not None:
            continue
        if isPrime(n):
            dp[n] = "Maria"
        else:
            prime_factor = False
            for i in range(2, n):
                if n % i == 0 and dp[i] == "Ben":
                    prime_factor = True
                    dp[n] = "Maria"
                    break
            if not prime_factor:
                dp[n] = "Ben"
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if dp[n] == "Maria":
            maria_wins += 1
        elif dp[n] == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
