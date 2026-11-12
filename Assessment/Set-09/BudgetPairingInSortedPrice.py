# Category B | October DSA Exam | Practice Assessment | Set 09 | Problem 1: Budget Pairing in Sorted Price
# --------------------------------------------------------------------------------------
# Given a sorted price list and target T, find two different 1-based positions
# whose values add up to T. Exactly one valid pair exists.
# Constraints:
# 2 <= n <= 10^5
# -10^9 <= price[i] <= 10^9
# Do not use extra memory proportional to n.
# --------------------------------------------------------------------------------------

def solution(prices, target):
    left = 0
    right = len(prices) - 1

    while left < right:
        current = prices[left] + prices[right]

        if current == target:
            return left + 1, right + 1
        elif current < target:
            left += 1
        else:
            right -= 1

    return -1, -1


if __name__ == "__main__":
    p1 = [3, 8, 12, 19, 25, 31, 40]
    print(solution(p1, 44))  # Output: (4, 5)

    p2 = [-5, -2, 0, 4, 9]
    print(solution(p2, 2))   # Output: (2, 4)

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Two Pointers
# --------------------------------------------------------------------------------------