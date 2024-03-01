#!/usr/bin/python3
""" making change problem """


def makeChange(coins, total):
    """ make change function """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            return count
        if total < coin:
            continue
        count += total // coin
        total = total % coin
    if total != 0:
        return -1
    return count
