"""Author: Joe Ferber
Created: Sept. 11, 2026
Find the largest profit from buying a stock and selling it later.
"""


def maxProfit(prices):
    profit = 0
    for buy in range(len(prices)):
        # Try each selling day that comes after the buying day.
        for sell in range(buy + 1, len(prices)):
            # Keep the largest profit found so far.
            profit = max(profit, prices[sell] - prices[buy])
    return profit


# Black-box tests check mixed, falling, rising, and equal prices.
assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0
assert maxProfit([1, 2, 3, 4]) == 3
assert maxProfit([3, 3, 3]) == 0

# Clear-box tests check empty loops and a single possible sale.
assert maxProfit([]) == 0
assert maxProfit([5]) == 0
assert maxProfit([1, 5]) == 4
assert maxProfit([5, 1]) == 0

if __name__ == "__main__":
    user_input = input("Enter stock prices separated by spaces: ")

    # Turn the entered prices into a list of integers.
    prices = []
    for i in user_input.split():
        prices.append(int(i))

    print("Maximum profit:", maxProfit(prices))
