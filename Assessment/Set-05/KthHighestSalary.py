# Category B | October DSA Exam | Practice Assessment | Set 05 | Problem 3: Kth Highest Salary
# --------------------------------------------------------------------------------------
# Find the k-th largest element using Quickselect and partitioning.
# Duplicate values count separately.
#
# Constraints:
# 1 <= k <= n <= 10^5
# 1 <= salary[i] <= 10^9
# Built-in sorting is prohibited.
# --------------------------------------------------------------------------------------

def solution(arr, k):
    n = len(arr)

    # Convert k-th largest to ascending order index.
    target = n - k

    left = 0
    right = n - 1

    while left <= right:

        # Choose middle element as pivot.
        pivot = arr[(left + right) // 2]

        # Three-way partition:
        # [left ... low-1]  < pivot
        # [low ... high]    = pivot
        # [high+1 ... right] > pivot

        low = left
        current = left
        high = right

        while current <= high:

            if arr[current] < pivot:
                arr[low], arr[current] = arr[current], arr[low]
                low += 1
                current += 1

            elif arr[current] > pivot:
                arr[current], arr[high] = arr[high], arr[current]
                high -= 1

            else:
                current += 1

        # Decide which partition contains the target index.
        if target < low:
            right = low - 1

        elif target > high:
            left = high + 1

        else:
            return pivot


if __name__ == "__main__":
    p1 = [40, 25, 60, 25, 90, 75, 60, 30, 50]
    print(solution(p1, 3))  # Output: 60

    p2 = [10, 20, 30, 40, 50]
    print(solution(p2, 1))  # Output: 50

    p3 = [10, 20, 30, 40, 50]
    print(solution(p3, 5))  # Output: 10

    p4 = [5, 5, 5, 5]
    print(solution(p4, 2))  # Output: 5

# --------------------------------------------------------------------------------------
# Time Complexity: O(n) average, O(n^2) worst case.
# Space Complexity: O(1) auxiliary space.
# Pattern: Quickselect + Three-way Partitioning
# --------------------------------------------------------------------------------------