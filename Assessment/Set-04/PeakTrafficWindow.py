# Category B | October DSA Exam | Practice Assessment | Set 04 | Problem 1: Peak Traffic Window
# --------------------------------------------------------------------------------------
# Find the maximum sum of any k consecutive elements.
#
# Constraints:
# 1 <= k <= n <= 10^5
# -10^4 <= count[i] <= 10^4
# No built-in sum(), max(), or slicing inside the loop.
# --------------------------------------------------------------------------------------

def solution(arr, k):
    window_sum = 0

    for i in range(k):
        window_sum += arr[i]

    largest = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]

        if window_sum > largest:
            largest = window_sum

    return largest


if __name__ == "__main__":
    # Test cases
    p1 = ([4, 2, 10, 1, 3, 9, 6, 5, 7], 3)
    print(solution(*p1))     # Output: 20

    p2 = ([1, 2, 3, 4, 5], 2)
    print(solution(*p2))     # Output: 9

    p3 = ([-5, -2, -8, -1], 2)
    print(solution(*p3))     # Output: -3

    p4 = ([7, 8, 9], 3)
    print(solution(*p4))     # Output: 24

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Fixed-Size Sliding Window
# --------------------------------------------------------------------------------------