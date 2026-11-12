# Category B | October DSA Exam | Practice Assessment | Set 07 | Problem 3: First Failing Nightly Build
# --------------------------------------------------------------------------------------
# Find the 1-based position of the first failing build (value 1).
# Return -1 if all builds passed.
#
# Constraints:
# 1 <= n <= 10^5
# Array contains 0s followed by 1s.
# --------------------------------------------------------------------------------------

def solution(arr):
    lo = 0
    hi = len(arr) - 1
    answer = -1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] == 1:
            answer = mid + 1
            hi = mid - 1

        else:
            lo = mid + 1

    return answer


if __name__ == "__main__":
    p1 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    print(solution(p1))  # Output: 7

    p2 = [0, 0, 0, 0]
    print(solution(p2))  # Output: -1

    p3 = [1, 1, 1, 1]
    print(solution(p3))  # Output: 1

    p4 = [0, 0, 1, 1, 1]
    print(solution(p4))  # Output: 3

# --------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search on Monotonic Predicate / First True
# --------------------------------------------------------------------------------------