# Category B | October DSA Exam | Practice Assessment | Set 05 | Problem 1: Mock Test Ranking Passes
# --------------------------------------------------------------------------------------
# Sort marks using Bubble Sort and count productive passes.
# A productive pass is one in which at least one swap occurs.
#
# Constraints:
# 1 <= n <= 2000
# 0 <= marks[i] <= 100
# --------------------------------------------------------------------------------------

def solution(arr):
    n = len(arr)
    productive_passes = 0

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped:
            productive_passes += 1
        else:
            break

    return arr, productive_passes


if __name__ == "__main__":
    p1 = [5, 1, 4, 2, 8]
    print(solution(p1))  # Output: ([1, 2, 4, 5, 8], 2)

    p2 = [1, 2, 3, 4]
    print(solution(p2))  # Output: ([1, 2, 3, 4], 0)

    p3 = [4, 3, 2, 1]
    print(solution(p3))  # Output: ([1, 2, 3, 4], 3)

# --------------------------------------------------------------------------------------
# Time Complexity: O(n^2) worst case, O(n) best case.
# Space Complexity: O(1)
# Pattern: Bubble Sort + Early Termination
# --------------------------------------------------------------------------------------