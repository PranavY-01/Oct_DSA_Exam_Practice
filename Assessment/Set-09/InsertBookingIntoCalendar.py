# Category B | October DSA Exam | Practice Assessment | Set 09 | Problem 5: Insert Booking Into Calendar
# --------------------------------------------------------------------------------------
# Insert a new interval into an already sorted, pairwise disjoint list.
# Merge all intervals that overlap or touch the new interval.
# Constraints:
# 1 <= n <= 10^5
# 0 <= start <= end <= 10^9
# Existing intervals are sorted and non-touching.
# No sorting is needed.
# --------------------------------------------------------------------------------------

def solution(intervals, new_interval):
    result = []
    start, end = new_interval
    i = 0
    n = len(intervals)

    # 1. Add intervals completely before the new interval.
    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    # 2. Merge all overlapping or touching intervals.
    while i < n and intervals[i][0] <= end:
        if intervals[i][0] < start:
            start = intervals[i][0]

        if intervals[i][1] > end:
            end = intervals[i][1]

        i += 1

    result.append([start, end])

    # 3. Add all remaining intervals.
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    p1 = [[1, 3], [6, 9], [12, 15], [18, 20], [22, 25]]
    print(solution(p1, [8, 13]))
    # Output: [[1, 3], [6, 15], [18, 20], [22, 25]]

    p2 = [[1, 2], [5, 7], [10, 12]]
    print(solution(p2, [3, 9]))
    # Output: [[1, 2], [3, 9], [10, 12]]

    p3 = [[2, 5], [8, 10]]
    print(solution(p3, [1, 12]))
    # Output: [[1, 12]]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pattern: Linear Traversal + Interval Merging
# --------------------------------------------------------------------------------------