# Category B | October DSA Exam | Practice Assessment | Set 07 | Problem 2: Student ID Insertion Point
# --------------------------------------------------------------------------------------
# Find the index of target t if present.
# Otherwise, return its sorted insertion position.
#
# Constraints:
# 1 <= n <= 10^5
# IDs are distinct and sorted.
# No bisect.
# --------------------------------------------------------------------------------------

def solution(arr, t):
    lo = 0
    hi = len(arr)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] < t:
            lo = mid + 1
        else:
            hi = mid

    return lo


if __name__ == "__main__":
    p1 = [10, 20, 30, 45, 60, 80]
    print(solution(p1, 50))  # Output: 4

    p2 = [10, 20, 30, 45, 60, 80]
    print(solution(p2, 30))  # Output: 2

    p3 = [10, 20, 30, 45, 60, 80]
    print(solution(p3, 5))   # Output: 0

    p4 = [10, 20, 30, 45, 60, 80]
    print(solution(p4, 100)) # Output: 6

# --------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Lower Bound Binary Search
# --------------------------------------------------------------------------------------