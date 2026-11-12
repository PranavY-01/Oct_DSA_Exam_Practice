# Category B | October DSA Exam | Practice Assessment | Set 06 | Problem 2: Warehouse Bin Sorting
# --------------------------------------------------------------------------------------
# Sort an array containing only 0, 1 and 2 using three pointers.
#
# Constraints:
# 1 <= n <= 10^5
# Each element is 0, 1 or 2.
# In-place, single-pass partitioning.
# --------------------------------------------------------------------------------------

def solution(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:

        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


if __name__ == "__main__":
    p1 = [2, 0, 1, 2, 1, 0, 1, 0]
    print(solution(p1))
    # Output: [0, 0, 0, 1, 1, 1, 2, 2]

    p2 = [0, 0, 0, 0]
    print(solution(p2))
    # Output: [0, 0, 0, 0]

    p3 = [2, 2, 1, 1, 0, 0]
    print(solution(p3))
    # Output: [0, 0, 1, 1, 2, 2]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n) - Single traversal.
# Space Complexity: O(1) - In-place swaps.
# Pattern: Dutch National Flag Algorithm / Three Pointers
# --------------------------------------------------------------------------------------