# Category B | October DSA Exam | Practice Assessment | Set 09 | Problem 4: Booking Overlap Consolidation
# --------------------------------------------------------------------------------------
# Merge all overlapping or touching closed intervals.
# Sort intervals by start using a custom sorting routine.
# Constraints:
# 1 <= n <= 10^5
# 0 <= start <= end <= 10^9
# Built-in sorting is not allowed.
# --------------------------------------------------------------------------------------

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def solution(intervals):
    intervals = merge_sort(intervals)

    merged = []

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            if end > merged[-1][1]:
                merged[-1][1] = end

    return merged


if __name__ == "__main__":
    p1 = [[8, 10], [1, 3], [2, 6], [15, 18], [17, 20], [6, 7]]
    print(solution(p1))
    # Output: [[1, 7], [8, 10], [15, 20]]

    p2 = [[1, 4], [4, 5], [5, 6], [8, 9]]
    print(solution(p2))
    # Output: [[1, 6], [8, 9]]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Pattern: Merge Sort + Interval Merging
# --------------------------------------------------------------------------------------