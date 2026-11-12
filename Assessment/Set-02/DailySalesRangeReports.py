# Category B | October DSA Exam | Practice Assessment | Set 02 | Problem 4: Daily Sales Range Reports
# --------------------------------------------------------------------------------------
# Build prefix sums and answer multiple range-sum queries.
# Each query asks for the sum of arr[l:r+1].
#
# Constraints:
# 1 <= n, q <= 10^5
# 0 <= sales[i] <= 10^4
# 0 <= l <= r <= n-1
# Do not use sum() or itertools.accumulate.
# --------------------------------------------------------------------------------------

def solution(arr, queries):
    n = len(arr)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    answers = []

    for l, r in queries:
        answers.append(prefix[r + 1] - prefix[l])

    return answers


if __name__ == "__main__":
    # Test cases
    p1 = (
        [5, 3, 8, 2, 7, 1, 9, 4],
        [(0, 2), (3, 5), (1, 7), (4, 4)]
    )
    print(solution(*p1))     # Output: [16, 10, 34, 7]

    p2 = (
        [10, 20, 30, 40],
        [(0, 3), (1, 2), (2, 2)]
    )
    print(solution(*p2))     # Output: [100, 50, 30]

    p3 = (
        [5, 10, 15],
        [(0, 0), (2, 2)]
    )
    print(solution(*p3))     # Output: [5, 15]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n + q)
# Space Complexity: O(n + q), including the output list
# Pattern: Prefix Sum
# --------------------------------------------------------------------------------------