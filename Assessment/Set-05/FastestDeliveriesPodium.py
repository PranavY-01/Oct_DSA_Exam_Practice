# Category B | October DSA Exam | Practice Assessment | Set 05 | Problem 2: Fastest Deliveries Podium
# --------------------------------------------------------------------------------------
# Find the k smallest delivery times using Selection Sort rounds.
#
# Constraints:
# 1 <= k <= n <= 3000
# 1 <= time[i] <= 10^4
# Do not use sort(), min(), or heaps.
# --------------------------------------------------------------------------------------

def solution(arr, k):
    n = len(arr)

    for i in range(k):
        min_index = i

        # Find the smallest element in the unsorted portion.
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Place the smallest element at position i.
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr[:k]


if __name__ == "__main__":
    p1 = [29, 14, 36, 7, 21, 14, 50]
    print(solution(p1, 3))  # Output: [7, 14, 14]

    p2 = [8, 3, 6, 1, 5]
    print(solution(p2, 2))  # Output: [1, 3]

    p3 = [4, 4, 2, 2, 1]
    print(solution(p3, 4))  # Output: [1, 2, 2, 4]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n * k)
# Space Complexity: O(1) auxiliary space (excluding returned slice).
# Pattern: Partial Selection Sort
# --------------------------------------------------------------------------------------