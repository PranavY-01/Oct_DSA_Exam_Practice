# Category B | October DSA Exam | Practice Assessment | Set 04 | Problem 3: Strong Average Days
# --------------------------------------------------------------------------------------
# Count the number of windows of exactly k consecutive days
# whose average attendance is at least T.
#
# Constraints:
# 1 <= k <= n <= 10^5
# 0 <= count[i] <= 10^4
# 1 <= T <= 10^4
# --------------------------------------------------------------------------------------

def solution(arr, k, T):
    window_sum = 0
    target = k * T

    for i in range(k):
        window_sum += arr[i]

    count = 0

    if window_sum >= target:
        count += 1

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]

        if window_sum >= target:
            count += 1

    return count


if __name__ == "__main__":
    # Test cases
    p1 = ([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
    print(solution(*p1))     # Output: 3

    p2 = ([10, 10, 10, 10], 2, 10)
    print(solution(*p2))     # Output: 3

    p3 = ([1, 2, 3, 4], 2, 10)
    print(solution(*p3))     # Output: 0

    p4 = ([5, 5, 5], 3, 5)
    print(solution(*p4))     # Output: 1

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Fixed-Size Sliding Window / Threshold Counting
# --------------------------------------------------------------------------------------