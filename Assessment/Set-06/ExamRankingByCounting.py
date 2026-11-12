# Category B | October DSA Exam | Practice Assessment | Set 06 | Problem 1: Exam Marks Ranking by Counting
# --------------------------------------------------------------------------------------
# Sort marks using Counting Sort.
#
# Constraints:
# 1 <= n <= 10^5
# 0 <= mark[i] <= 100
# No built-in sorting or Counter.
# --------------------------------------------------------------------------------------

def solution(arr):
    count = [0] * 101

    # Count frequency of every mark.
    for mark in arr:
        count[mark] += 1

    # Rebuild the array in ascending order.
    index = 0

    for mark in range(101):
        while count[mark] > 0:
            arr[index] = mark
            index += 1
            count[mark] -= 1

    return arr


if __name__ == "__main__":
    p1 = [78, 92, 65, 78, 100, 0, 65, 92, 78, 55]
    print(solution(p1))
    # Output: [0, 55, 65, 65, 78, 78, 78, 92, 92, 100]

    p2 = [50, 50, 50, 50]
    print(solution(p2))
    # Output: [50, 50, 50, 50]

    p3 = [100, 0, 100, 0, 50]
    print(solution(p3))
    # Output: [0, 0, 50, 100, 100]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n + 101) = O(n)
# Space Complexity: O(101) = O(1), fixed-size frequency array.
# Pattern: Counting Sort
# --------------------------------------------------------------------------------------