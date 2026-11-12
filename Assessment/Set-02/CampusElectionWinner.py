# Category B | October DSA Exam | Practice Assessment | Set 02 | Problem 1: Campus Election Winner
# --------------------------------------------------------------------------------------
# Find the candidate ID appearing more than n // 2 times.
# A majority candidate is guaranteed to exist.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= ID <= 10^9
# --------------------------------------------------------------------------------------

def solution(arr):
    candidate = None
    count = 0

    for value in arr:
        if count == 0:
            candidate = value

        if value == candidate:
            count += 1
        else:
            count -= 1

    return candidate


if __name__ == "__main__":
    # Test cases
    p1 = [3, 2, 3, 3, 1, 3, 2, 3, 3]
    print(solution(p1))     # Output: 3

    p2 = [2, 2, 1, 2, 3, 2, 2]
    print(solution(p2))     # Output: 2

    p3 = [7]
    print(solution(p3))     # Output: 7

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Boyer-Moore Voting Algorithm
# --------------------------------------------------------------------------------------