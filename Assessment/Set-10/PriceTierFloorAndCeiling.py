# Category B | October DSA Exam | Practice Assessment | Set 10 | Problem 2: Price Tier Floor and Ceiling
# --------------------------------------------------------------------------------------
# Find the largest value <= q (floor) and smallest value >= q (ceiling).
# Print None if either value does not exist.
# Constraints:
# 1 <= n <= 10^5
# -10^9 <= price, q <= 10^9
# Use binary search.
# --------------------------------------------------------------------------------------

def solution(arr, q):
    left = 0
    right = len(arr) - 1

    floor_val = None

    # Find the rightmost value <= q.
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= q:
            floor_val = arr[mid]
            left = mid + 1
        else:
            right = mid - 1

    left = 0
    right = len(arr) - 1

    ceiling_value = None

    # Find the leftmost value >= q.
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= q:
            ceiling_value = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return floor_val, ceiling_value


if __name__ == "__main__":
    p1 = [10, 20, 30, 40, 50, 60]
    print(solution(p1, 35))  # Output: (30, 40)

    p2 = [10, 20, 30]
    print(solution(p2, 5))   # Output: (None, 10)

    p3 = [10, 20, 30]
    print(solution(p3, 40))  # Output: (30, None)

    p4 = [10, 20, 20, 30]
    print(solution(p4, 20))  # Output: (20, 20)

# --------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search (Floor and Ceiling)
# --------------------------------------------------------------------------------------