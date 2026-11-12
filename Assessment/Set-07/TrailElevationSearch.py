# Category B | October DSA Exam | Practice Assessment | Set 07 | Problem 5: Trail Elevation Search
# --------------------------------------------------------------------------------------
# Find the smallest index of target h in a mountain array.
# First find the peak, then search the increasing and decreasing halves.
#
# Constraints:
# 3 <= n <= 10^5
# Array strictly increases, then strictly decreases.
# Peak is strictly inside the array.
# Required complexity: O(log n).
# --------------------------------------------------------------------------------------

def solution(arr, h):
    n = len(arr)

    # Step 1: Find the peak index.
    lo = 0
    hi = n - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    peak = lo

    # Step 2: Search the increasing half.
    lo = 0
    hi = peak

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] == h:
            return mid

        elif arr[mid] < h:
            lo = mid + 1

        else:
            hi = mid - 1

    # Step 3: Search the decreasing half.
    lo = peak + 1
    hi = n - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] == h:
            return mid

        elif arr[mid] < h:
            hi = mid - 1

        else:
            lo = mid + 1

    return -1


if __name__ == "__main__":
    p1 = [2, 5, 9, 14, 20, 17, 11, 6, 1]
    print(solution(p1, 11))  # Output: 6

    p2 = [2, 5, 9, 14, 20, 17, 11, 6, 1]
    print(solution(p2, 20))  # Output: 4

    p3 = [2, 5, 9, 14, 20, 17, 11, 6, 1]
    print(solution(p3, 3))   # Output: -1

    p4 = [1, 4, 8, 12, 10, 6, 2]
    print(solution(p4, 6))   # Output: 5

# --------------------------------------------------------------------------------------
# Time Complexity: O(log n) - Peak search + at most two binary searches.
# Space Complexity: O(1)
# Pattern: Mountain Array + Binary Search
# --------------------------------------------------------------------------------------