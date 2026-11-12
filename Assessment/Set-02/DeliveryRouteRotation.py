# Category B | October DSA Exam | Practice Assessment | Set 02 | Problem 5: Delivery Route Rotation
# --------------------------------------------------------------------------------------
# Rotate the array to the right by k positions, in-place.
# Use explicit loops and swaps. Do not use slicing or reversal helpers.
#
# Constraints:
# 1 <= n <= 10^5
# 0 <= k <= 10^9
# 1 <= stopID[i] <= 10^9
# --------------------------------------------------------------------------------------

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def solution(arr, k):
    n = len(arr)

    k = k % n

    if k == 0:
        return arr

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

    return arr


if __name__ == "__main__":
    # Test cases
    p1 = ([1, 2, 3, 4, 5, 6, 7], 3)
    print(solution(*p1))     # Output: [5, 6, 7, 1, 2, 3, 4]

    p2 = ([1, 2, 3, 4, 5], 2)
    print(solution(*p2))     # Output: [4, 5, 1, 2, 3]

    p3 = ([1, 2, 3], 3)
    print(solution(*p3))     # Output: [1, 2, 3]

    p4 = ([10, 20, 30, 40], 0)
    print(solution(*p4))     # Output: [10, 20, 30, 40]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Array Rotation / Three Reversals
# --------------------------------------------------------------------------------------