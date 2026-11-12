# Category B | October DSA Exam | Practice Assessment | Set 01 | Problem 4: Warehouse Balance Point
# --------------------------------------------------------------------------------------
# Find the leftmost index where the sum of elements to its left equals
# the sum of elements to its right. Exclude the current element.
# Return -1 if no balance point exists.
#
# Constraints:
# 1 <= n <= 10^5
# -1000 <= change[i] <= 1000
# --------------------------------------------------------------------------------------

def solution(arr):
    total = 0

    for value in arr:
        total += value

    left_sum = 0

    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1


if __name__ == "__main__":
    # Test cases
    p1 = [3, -2, 5, 4, 1, 5]
    print(solution(p1))     # Output: 3

    p2 = [1, 7, 3, 6, 5, 6]
    print(solution(p2))     # Output: 3

    p3 = [1, 2, 3]
    print(solution(p3))     # Output: -1

    p4 = [0]
    print(solution(p4))     # Output: 0

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Prefix Sum / Running Sum
# --------------------------------------------------------------------------------------