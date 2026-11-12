# Category B | October DSA Exam | Practice Assessment | Set 10 | Problem 1: Sensor Deviation Magnitudes
# --------------------------------------------------------------------------------------
# Given a sorted array, print the squares in non-decreasing order.
# Do not use built-in sorting.
# Constraints:
# 1 <= n <= 10^5
# -10^4 <= value <= 10^4
# --------------------------------------------------------------------------------------

def solution(arr):
    left = 0
    right = len(arr) - 1

    result = [0] * len(arr)
    pos = len(arr) - 1

    while left <= right:
        left_sq = arr[left] * arr[left]
        right_sq = arr[right] * arr[right]

        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1

        pos -= 1

    return result


if __name__ == "__main__":
    p1 = [-9, -4, -2, 0, 3, 5, 8]
    print(solution(p1))
    # Output: [0, 4, 9, 16, 25, 64, 81]

    p2 = [-5, -3, -1]
    print(solution(p2))
    # Output: [1, 9, 25]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pattern: Two Pointers
# --------------------------------------------------------------------------------------