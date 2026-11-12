# Category B | October DSA Exam | Practice Assessment | Set 03 | Problem 4: Merge Two Warehouse Stock Lists
# --------------------------------------------------------------------------------------
# Merge sorted array B into A.
# A has m real elements followed by n placeholder positions.
# Perform the merge in-place without creating a third array.
#
# Constraints:
# 0 <= m, n <= 10^5
# m + n >= 1
# -10^9 <= value <= 10^9
# Both arrays are sorted in non-decreasing order.
# --------------------------------------------------------------------------------------

def solution(A, B, m, n):
    i = m - 1
    j = n - 1
    write = m + n - 1

    while i >= 0 and j >= 0:

        if A[i] > B[j]:
            A[write] = A[i]
            i -= 1
        else:
            A[write] = B[j]
            j -= 1

        write -= 1

    while j >= 0:
        A[write] = B[j]
        j -= 1
        write -= 1

    return A


if __name__ == "__main__":
    # Test cases
    p1 = ([1, 4, 7, 10, 0, 0, 0], [2, 5, 8], 4, 3)
    print(solution(*p1))     # Output: [1, 2, 4, 5, 7, 8, 10]

    p2 = ([1, 2, 3, 0, 0], [4, 5], 3, 2)
    print(solution(*p2))     # Output: [1, 2, 3, 4, 5]

    p3 = ([0, 0, 0], [1, 2, 3], 0, 3)
    print(solution(*p3))     # Output: [1, 2, 3]

    p4 = ([1, 3, 5], [], 3, 0)
    print(solution(*p4))     # Output: [1, 3, 5]

# --------------------------------------------------------------------------------------
# Time Complexity: O(m + n)
# Space Complexity: O(1)
# Pattern: Two Pointers / In-place Merge
# --------------------------------------------------------------------------------------