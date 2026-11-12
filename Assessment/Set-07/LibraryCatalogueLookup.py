# Category B | October DSA Exam | Practice Assessment | Set 07 | Problem 1: Library Catalogue Lookup
# --------------------------------------------------------------------------------------
# Find the 0-based index of q using Binary Search.
#
# Constraints:
# 1 <= n <= 10^5
# IDs are distinct and sorted in increasing order.
# No bisect or list.index.
# --------------------------------------------------------------------------------------

def solution(arr, q):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] == q:
            return mid

        elif arr[mid] < q:
            lo = mid + 1

        else:
            hi = mid - 1

    return -1


if __name__ == "__main__":
    p1 = [102, 118, 130, 145, 160, 177, 190, 204, 230]
    print(solution(p1, 177))  # Output: 5

    p2 = [10, 20, 30, 40, 50]
    print(solution(p2, 25))   # Output: -1

    p3 = [10, 20, 30, 40, 50]
    print(solution(p3, 10))   # Output: 0

    p4 = [10, 20, 30, 40, 50]
    print(solution(p4, 50))   # Output: 4

# --------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Classic Binary Search
# --------------------------------------------------------------------------------------