# Category B | October DSA Exam | Practice Assessment | Set 01 | Problem 1: Gift Card Pairing At Checkout
# --------------------------------------------------------------------------------------
# Given an array of prices and target T, find two distinct indices whose values
# add up to T. Return the indices in ascending order.
#
# Constraints:
# 2 <= n <= 10^5
# 1 <= price[i] <= 10^9
# 1 <= T <= 2 * 10^9
# Exactly one valid pair exists.
# --------------------------------------------------------------------------------------

def solution(prices, T):
    seen = {}

    for i in range(len(prices)):
        complement = T - prices[i]

        if complement in seen:
            return seen[complement], i

        seen[prices[i]] = i


if __name__ == "__main__":
    # Test cases
    p1 = ([120, 45, 80, 200, 35, 150], 235)
    print(solution(*p1))     # Output: (3, 4)

    p2 = ([2, 7, 11, 15], 9)
    print(solution(*p2))     # Output: (0, 1)

    p3 = ([3, 3], 6)
    print(solution(*p3))     # Output: (0, 1)

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the prices array
# Space Complexity: O(n)
# Pattern: Hash Map / Complement Lookup
# --------------------------------------------------------------------------------------