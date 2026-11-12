# Category B | October DSA Exam | Practice Assessment | Set 05 | Problem 3: Nearly Sorted Event Log
# --------------------------------------------------------------------------------------
# Sort timestamps using Insertion Sort and count individual shifts.
#
# Constraints:
# 1 <= n <= 5000
# 0 <= timestamp[i] <= 10^6
# --------------------------------------------------------------------------------------

def solution(arr):
    n = len(arr)
    shifts = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements greater than key one position right.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1

        arr[j + 1] = key

    return arr, shifts


if __name__ == "__main__":
    p1 = [10, 20, 15, 30, 40, 35, 50, 45]
    print(solution(p1))  # Output: ([10, 15, 20, 30, 35, 40, 45, 50], 3)

    p2 = [1, 2, 3, 4]
    print(solution(p2))  # Output: ([1, 2, 3, 4], 0)

    p3 = [5, 4, 3, 2, 1]
    print(solution(p3))  # Output: ([1, 2, 3, 4, 5], 10)

# --------------------------------------------------------------------------------------
# Time Complexity: O(n^2) worst case, O(n) best case.
# Space Complexity: O(1)
# Pattern: Insertion Sort + Shift Counting
# --------------------------------------------------------------------------------------
