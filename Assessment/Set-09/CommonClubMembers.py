# Category B | October DSA Exam | Practice Assessment | Set 09 | Problem 3: Common Club Members
# --------------------------------------------------------------------------------------
# Find distinct IDs present in both arrays.
# Print common IDs in increasing order, or None if no common ID exists.
# Constraints:
# 1 <= m, n <= 10^5
# 1 <= ID <= 10^9
# Use a hash set for membership and custom sorting.
# Do not use set operators, sorted(), or list.sort().
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


def solution(A, B):
    members = set(A)
    common = set()

    for student_id in B:
        if student_id in members:
            common.add(student_id)

    if len(common) == 0:
        return None

    return merge_sort(list(common))


if __name__ == "__main__":
    A = [9, 4, 9, 5, 12, 4]
    B = [12, 9, 9, 8, 4, 12]
    print(solution(A, B))  # Output: [4, 9, 12]

    A = [1, 3, 5]
    B = [2, 4, 6]
    print(solution(A, B))  # Output: None

# --------------------------------------------------------------------------------------
# Time Complexity: O(m + n + k log k) average
# Space Complexity: O(m + n + k)
# k = number of distinct common IDs
# Pattern: Hash Set + Merge Sort
# --------------------------------------------------------------------------------------