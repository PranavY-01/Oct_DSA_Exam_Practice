# Category B | October DSA Exam | Practice Assessment | Set 06 | Problem 4: Product Popularity Ordering
# --------------------------------------------------------------------------------------
# Sort product IDs by:
# 1. Frequency ascending.
# 2. Product ID descending when frequencies are equal.
# All copies of each ID must be consecutive.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= ID <= 10^9
# No sorting(), sorted(), or Counter.
# --------------------------------------------------------------------------------------

def solution(arr):
    freq = {}

    for value in arr:
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1

    unique_ids = list(freq.keys())

    # Custom comparison:
    # Lower frequency comes first.
    # If equal, larger ID comes first.
    def comes_before(a, b):
        if freq[a] != freq[b]:
            return freq[a] < freq[b]

        return a > b

    def merge_sort(items):
        if len(items) <= 1:
            return items

        mid = len(items) // 2

        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])

        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if comes_before(left[i], right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    ordered_ids = merge_sort(unique_ids)

    result = []

    for value in ordered_ids:
        for _ in range(freq[value]):
            result.append(value)

    return result


if __name__ == "__main__":
    p1 = [4, 4, 6, 2, 2, 2, 6, 9, 6]
    print(solution(p1))
    # Output: [9, 4, 4, 6, 6, 6, 2, 2, 2]

    p2 = [5, 5, 3, 3, 1, 1]
    print(solution(p2))
    # Output: [5, 5, 3, 3, 1, 1]

    p3 = [10, 10, 10, 20, 30, 30]
    print(solution(p3))
    # Output: [20, 30, 30, 10, 10, 10]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n + u log u), where u is the number of unique IDs.
# Space Complexity: O(n + u) for frequency map, merge results and output.
# Pattern: Hash Map + Custom Comparator + Merge Sort
# --------------------------------------------------------------------------------------