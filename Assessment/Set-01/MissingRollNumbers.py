# Category B | October DSA Exam | Practice Assessment | Set 01 | Problem 5: Missing Roll Numbers
# --------------------------------------------------------------------------------------
# Given an array of n integers ranging from 1 to n, find all missing numbers.
# Modify the original array to track which values have appeared.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= arr[i] <= n
# Avoid creating an extra tracking array.
# --------------------------------------------------------------------------------------

def solution(arr):
    n = len(arr)

    for i in range(n):
        index = abs(arr[i]) - 1

        if arr[index] > 0:
            arr[index] = -arr[index]

    missing = []

    for i in range(n):
        if arr[i] > 0:
            missing.append(i + 1)

    if len(missing) == 0:
        return None

    return missing


if __name__ == "__main__":
    # Test cases
    p1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(solution(p1))     # Output: [5, 6]

    p2 = [1, 1]
    print(solution(p2))     # Output: [2]

    p3 = [1, 2, 3, 4, 5]
    print(solution(p3))     # Output: None

    p4 = [2, 2, 2, 2]
    print(solution(p4))     # Output: [1, 3, 4]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary, excluding output list
# Pattern: In-place Index Marking / Cyclic Sign Marking
# --------------------------------------------------------------------------------------