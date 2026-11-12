# Category B | October DSA Exam | Practice Assessment | Set 01 | Problem 2: First Duplicate Ticket Scan
# --------------------------------------------------------------------------------------
# Find the first value that appears for a second time while traversing the array.
# Return -1 if no duplicate exists.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= ID <= 10^9
# --------------------------------------------------------------------------------------

def solution(ids):
    seen = set()

    for value in ids:
        if value in seen:
            return value

        seen.add(value)

    return -1


if __name__ == "__main__":
    # Test cases
    p1 = [4021, 3377, 5120, 3377, 4021, 9001, 5120, 7]
    print(solution(p1))     # Output: 3377

    p2 = [1, 2, 3, 4, 5]
    print(solution(p2))     # Output: -1

    p3 = [5, 5, 2, 2]
    print(solution(p3))     # Output: 5

# --------------------------------------------------------------------------------------
# Time Complexity: O(n) average
# Space Complexity: O(n)
# Pattern: Hash Set / Duplicate Detection
# --------------------------------------------------------------------------------------