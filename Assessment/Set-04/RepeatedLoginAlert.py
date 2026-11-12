# Category B | October DSA Exam | Practice Assessment | Set 04 | Problem 2: Repeated Login Alert
# --------------------------------------------------------------------------------------
# Check whether any duplicate values occur at positions i and j
# where i < j and j - i <= k.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= k <= 10^5
# 1 <= ID <= 10^9
# --------------------------------------------------------------------------------------

def solution(arr, k):
    last_seen = {}

    for i in range(len(arr)):
        value = arr[i]

        if value in last_seen:
            if i - last_seen[value] <= k:
                return "YES"

        last_seen[value] = i

    return "NO"


if __name__ == "__main__":
    # Test cases
    p1 = ([7, 12, 5, 7, 12, 9, 12, 4], 2)
    print(solution(*p1))     # Output: YES

    p2 = ([1, 2, 3, 1], 2)
    print(solution(*p2))     # Output: NO

    p3 = ([5, 5], 1)
    print(solution(*p3))     # Output: YES

    p4 = ([1, 2, 3, 4], 3)
    print(solution(*p4))     # Output: NO

# --------------------------------------------------------------------------------------
# Time Complexity: O(n) average
# Space Complexity: O(n)
# Pattern: Hash Map / Last Seen Index
# --------------------------------------------------------------------------------------