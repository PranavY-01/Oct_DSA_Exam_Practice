# Category B | October DSA Exam | Practice Assessment | Set 08 | Problem 3: Earliest Slot After Shift Challenge
# --------------------------------------------------------------------------------------
# Find the minimum element in a rotated sorted array.
#
# Constraints:
# 1 <= n <= 10^5
# All values are distinct.
# No min() or linear scan.
# --------------------------------------------------------------------------------------

def solution(arr):
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] > arr[hi]:
            # Minimum is in the right half.
            lo = mid + 1
        else:
            # Minimum is at mid or in the left half.
            hi = mid

    return arr[lo]


if __name__ == "__main__":
    p1 = [40, 50, 60, 70, 10, 20, 30]
    print(solution(p1))  # Output: 10

    p2 = [4, 5, 6, 7, 0, 1, 2]
    print(solution(p2))  # Output: 0

    p3 = [1, 2, 3, 4, 5]
    print(solution(p3))  # Output: 1

    p4 = [2, 1]
    print(solution(p4))  # Output: 1

# --------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search in Rotated Sorted Array
# --------------------------------------------------------------------------------------