# Category B | October DSA Exam | Practice Assessment | Set 08 | Problem 1: Square Tile Floor Planner
# --------------------------------------------------------------------------------------
# Given a rectangular floor of dimensions m x n, find the minimum number of square tiles needed to cover it.
# All tiles must be of the same size and cover the entire floor without overlapping.
#
# Constraints:
# 1 <= m, n <= 10^9
# --------------------------------------------------------------------------------------

def solution(m, n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    g = gcd(m, n)
    return (m // g) * (n // g)


if __name__ == "__main__":
    print(solution(4, 6))  # Output: 6

    print(solution(3, 5))  # Output: 15

    print(solution(2, 4))  # Output: 2

# --------------------------------------------------------------------------------------
# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)
# Pattern: GCD + Area Calculation
# --------------------------------------------------------------------------------------