# Category B | October DSA Exam | Practice Assessment | Set 06 | Problem 5: Sensor Readings with Heavy Duplicates
# --------------------------------------------------------------------------------------
# Sort readings using iterative 3-way Quicksort.
# Uses an explicit stack instead of recursion.
#
# Constraints:
# 1 <= n <= 10^5
# 0 <= reading[i] <= 10^9
# Middle element is selected as pivot.
# Built-in sorting is prohibited.
# --------------------------------------------------------------------------------------

def solution(arr):
    n = len(arr)

    if n <= 1:
        return arr

    # Store index ranges that still need sorting.
    stack = [(0, n - 1)]

    while stack:
        left, right = stack.pop()

        if left >= right:
            continue

        # Select middle element as pivot.
        pivot = arr[(left + right) // 2]

        # Three-way partition pointers.
        low = left
        mid = left
        high = right

        while mid <= high:

            if arr[mid] < pivot:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1

            elif arr[mid] > pivot:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

            else:
                mid += 1

        # Equal region [low ... high] is already sorted.
        # Only process the smaller and larger regions.
        if left < low - 1:
            stack.append((left, low - 1))

        if high + 1 < right:
            stack.append((high + 1, right))

    return arr


if __name__ == "__main__":
    p1 = [3, 1, 3, 2, 3, 1, 2, 3, 1, 3]
    print(solution(p1))
    # Output: [1, 1, 1, 2, 2, 3, 3, 3, 3, 3]

    p2 = [5, 5, 5, 5, 5]
    print(solution(p2))
    # Output: [5, 5, 5, 5, 5]

    p3 = [9, 7, 5, 3, 1]
    print(solution(p3))
    # Output: [1, 3, 5, 7, 9]

    p4 = [1, 2, 3, 4, 5]
    print(solution(p4))
    # Output: [1, 2, 3, 4, 5]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n log n) average, O(n^2) worst case.
# Space Complexity: O(n) worst case for the explicit stack.
# Pattern: Iterative Quicksort + Dutch National Flag Partitioning
# --------------------------------------------------------------------------------------