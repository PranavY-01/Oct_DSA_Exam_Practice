# Category B | October DSA Exam | Practice Assessment | Set 06 | Problem 3: Combined Attendee List
# --------------------------------------------------------------------------------------
# Find the union of two sorted lists without duplicates.
#
# Constraints:
# 0 <= m, n <= 10^5, m + n >= 1
# Both lists are strictly increasing.
# Built-in sorting is prohibited.
# --------------------------------------------------------------------------------------

def solution(A, B):
    i = 0
    j = 0
    result = []

    while i < len(A) and j < len(B):

        if A[i] < B[j]:
            result.append(A[i])
            i += 1

        elif A[i] > B[j]:
            result.append(B[j])
            j += 1

        else:
            # Same ID in both lists: add only once.
            result.append(A[i])
            i += 1
            j += 1

    # Append remaining elements from A.
    while i < len(A):
        result.append(A[i])
        i += 1

    # Append remaining elements from B.
    while j < len(B):
        result.append(B[j])
        j += 1

    return result


if __name__ == "__main__":
    p1 = [3, 8, 12, 20, 25]
    p2 = [5, 8, 20, 31]
    print(solution(p1, p2))
    # Output: [3, 5, 8, 12, 20, 25, 31]

    p3 = []
    p4 = [1, 2, 3]
    print(solution(p3, p4))
    # Output: [1, 2, 3]

    p5 = [1, 3, 5]
    p6 = [2, 4, 6]
    print(solution(p5, p6))
    # Output: [1, 2, 3, 4, 5, 6]

# --------------------------------------------------------------------------------------
# Time Complexity: O(m + n)
# Space Complexity: O(m + n) - Result array.
# Pattern: Two Pointers + Merge of Sorted Arrays
# --------------------------------------------------------------------------------------