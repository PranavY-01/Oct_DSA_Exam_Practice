# Category B | October DSA Exam | Practice Assessment | Set 02 | Problem 2: First Unique Visitor
# --------------------------------------------------------------------------------------
# Find the first ID whose frequency in the entire array is exactly one.
# Return -1 if no such ID exists.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= ID <= 10^9
# --------------------------------------------------------------------------------------

def solution(arr):
    frequency = {}

    for value in arr:
        frequency[value] = frequency.get(value, 0) + 1

    for value in arr:
        if frequency[value] == 1:
            return value

    return -1


if __name__ == "__main__":
    # Test cases
    p1 = [17, 23, 17, 8, 23, 42, 8, 5, 42, 17]
    print(solution(p1))     # Output: 5

    p2 = [4, 4, 7, 7, 9, 9]
    print(solution(p2))     # Output: -1

    p3 = [10, 20, 30]
    print(solution(p3))     # Output: 10

# --------------------------------------------------------------------------------------
# Time Complexity: O(n) average
# Space Complexity: O(n)
# Pattern: Hash Map / Frequency Counting
# --------------------------------------------------------------------------------------