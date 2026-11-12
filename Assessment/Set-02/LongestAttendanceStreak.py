# Category B | October DSA Exam | Practice Assessment | Set 02 | Problem 3: Longest Attendance Streak
# --------------------------------------------------------------------------------------
# Find the longest consecutive run where every attendance value >= T.
# Return 0 if no good day exists.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= T <= 10^4
# 0 <= attendance[i] <= 10^4
# --------------------------------------------------------------------------------------

def solution(arr, T):
    current = 0
    longest = 0

    for value in arr:
        if value >= T:
            current += 1

            if current > longest:
                longest = current
        else:
            current = 0

    return longest


if __name__ == "__main__":
    # Test cases
    p1 = ([28, 35, 40, 31, 30, 12, 33, 36, 29, 41], 30)
    print(solution(*p1))     # Output: 4

    p2 = ([10, 20, 30, 40, 50], 30)
    print(solution(*p2))     # Output: 3

    p3 = ([10, 15, 20], 30)
    print(solution(*p3))     # Output: 0

    p4 = ([35, 35, 35, 35], 30)
    print(solution(*p4))     # Output: 4

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Linear Traversal / Consecutive Sequence Tracking
# --------------------------------------------------------------------------------------