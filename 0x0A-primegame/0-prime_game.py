#!/usr/bin/python3
def is_Prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_winner(n):
    # if n is even, ben wins bacause Maria cannot pick 2
    if n % 2 == 0:
        return "Ben"
    # If n is odd and prime, Maria wins because she can pick n itself
    elif is_Prime(n):
        return "Maria"
    else:
        return "Ben"


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = get_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
