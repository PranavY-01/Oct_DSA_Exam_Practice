# Category B | October DSA Exam | Practice Assessment | Set 09 | Problem 3: Judges Trimmed Mean
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# Sort scores, discard t smallest and t largest values, then calculate
# the mean of the remaining scores with exactly two decimal places.
# Constraints:
# 1 <= n <= 10^5
# 0 <= t and n - 2*t >= 1
# 0 <= score <= 100
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
        if left[i] <= right[j]:
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


def solution(scores, t):
    scores = merge_sort(scores)

    total = 0
    for i in range(t, len(scores) - t):
        total += scores[i]

    count = len(scores) - 2 * t
    return total / count


if __name__ == "__main__":
    p1 = [8, 9, 7, 10, 6, 9, 5, 8, 9, 10]
    print("%.2f" % solution(p1, 1))  # Output: 8.25

    p2 = [10, 20, 30]
    print("%.2f" % solution(p2, 1))  # Output: 20.00

# --------------------------------------------------------------------------------------
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Pattern: Merge Sort + Array Traversal
# --------------------------------------------------------------------------------------