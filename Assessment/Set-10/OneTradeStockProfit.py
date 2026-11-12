# Category B | October DSA Exam | Practice Assessment | Set 10 | Problem 3: One Trade Stock Profit
# --------------------------------------------------------------------------------------
# Find maximum price[j] - price[i] where i < j.
# Return 0 if no profitable trade exists.
# Constraints:
# 1 <= n <= 10^5
# 1 <= price <= 10^9
# Do not use built-in max() or min().
# --------------------------------------------------------------------------------------

def solution(prices):
    min_price = prices[0]
    best_profit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - min_price

        if profit > best_profit:
            best_profit = profit

        if prices[i] < min_price:
            min_price = prices[i]

    return best_profit


if __name__ == "__main__":
    p1 = [120, 98, 105, 90, 112, 130, 95, 118]
    print(solution(p1))  # Output: 40

    p2 = [9, 7, 5, 3, 1]
    print(solution(p2))  # Output: 0

    p3 = [5]
    print(solution(p3))  # Output: 0

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Greedy + Single Pass
# --------------------------------------------------------------------------------------