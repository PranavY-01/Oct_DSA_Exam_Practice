# Category B | October DSA Exam | Practice Assessment | Set 08 | Problem 4: Rotated Log Lookup
# --------------------------------------------------------------------------------------
# Given a rotated sorted array of distinct integers, find the index of target h.
# Return -1 if h is absent.
#
# Constraints:
# 1 <= n <= 10^5
# All values are distinct.
# No linear scan.
# --------------------------------------------------------------------------------------

def solution(arr, t):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2   # Prevent overflow

        if arr[mid] == t:
            return mid

        # Check whether the left half is sorted.
        if arr[lo] <= arr[mid]:

            # Target belongs to the sorted left half.
            if arr[lo] <= t < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        # Otherwise, the right half is sorted.
        else:

            # Target belongs to the sorted right half.
            if arr[mid] < t <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1


if __name__ == "__main__":
    p1 = [15, 18, 22, 31, 3, 6, 9, 12]
    print(solution(p1, 9))   # Output: 6

    p2 = [4, 5, 6, 7, 0, 1, 2]
    print(solution(p2, 0))   # Output: 4

    p3 = [4, 5, 6, 7, 0, 1, 2]
    print(solution(p3, 3))   # Output: -1

    p4 = [1, 2, 3, 4, 5]
    print(solution(p4, 4))   # Output: 3

# --------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Modified Binary Search / Rotated Array Search
# --------------------------------------------------------------------------------------