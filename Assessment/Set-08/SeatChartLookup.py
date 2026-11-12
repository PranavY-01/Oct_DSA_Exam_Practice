# Category B | October DSA Exam | Practice Assessment | Set 08 | Problem 2: Seat Chart Lookup
# --------------------------------------------------------------------------------------
# Search a sorted matrix using virtual 1D binary search.
#
# Constraints:
# 1 <= R, C <= 300
# Matrix rows and overall sequence are sorted.
# Do not create a flattened list.
# --------------------------------------------------------------------------------------

def solution(matrix, t):
    rows = len(matrix)
    cols = len(matrix[0])

    lo = 0
    hi = rows * cols - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        # Convert virtual 1D index into 2D coordinates.
        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == t:
            return [row, col]

        elif value < t:
            lo = mid + 1

        else:
            hi = mid - 1

    return [-1, -1]


if __name__ == "__main__":
    p1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]

    print(solution(p1, 16))  # Output: [1, 2]
    print(solution(p1, 13))  # Output: [-1, -1]
    print(solution(p1, 1))   # Output: [0, 0]
    print(solution(p1, 60))  # Output: [2, 3]

# --------------------------------------------------------------------------------------
# Time Complexity: O(log(R * C))
# Space Complexity: O(1)
# Pattern: Binary Search on 2D Matrix
# --------------------------------------------------------------------------------------