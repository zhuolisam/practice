# Question:
# You are given an array of objects representing items to be put in a knapsack. The objects have 3
# attributes: name, weight, and value. The items need to be selected so that the total weight does not
# exceed the maximum weight and the value is maximized.

# Solution:
# This is a classic knapsack problem. I will share some solution.
# 1. Naive recursion. Each function calls decide if we pick the current item. The time complexiity is O(2^n).
# 2. Bottom-up dynamic programming. We store each subproblem in a table. The time complexity is O(nW) where n is the number of items and W is the maximum weight. Time complexity and space complexity are both O(nW).
# I'm implementing the second solution, which is more efficient.

def knapsack(items, max_weight) -> int:
    """_summary_

    Args:
        items (Dict): Dict with name, weight, and value
        max_weight (int): Maximum weight

    Returns:
        int: Max value
    """
    n = len(items)
    # table with one extra dummy row and column
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if items[i - 1]['weight'] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - items[i - 1]['weight']] +
                    items[i - 1]['value']
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_weight]
