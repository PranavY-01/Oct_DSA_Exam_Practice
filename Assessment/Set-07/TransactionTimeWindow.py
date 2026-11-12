# Category B | October DSA Exam | Practice Assessment | Set 07 | Problem 4: Transaction Time Window
# --------------------------------------------------------------------------------------
# Find the first and last occurrence of target x.
# Return [-1, -1] if x is absent.
#
# Constraints:
# 1 <= n <= 10^5
# Array is sorted in non-decreasing order.
# Duplicates are allowed.
# No bisect or linear scanning.
# --------------------------------------------------------------------------------------

def solution(arr, x):

    def find_first():
        lo = 0
        hi = len(arr) - 1
        answer = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == x:
                answer = mid
                hi = mid - 1

            elif arr[mid] < x:
                lo = mid + 1

            else:
                hi = mid - 1

        return answer

    def find_last():
        lo = 0
        hi = len(arr) - 1
        answer = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == x:
                answer = mid
                lo = mid + 1

            elif arr[mid] < x:
                lo = mid + 1

            else:
                hi = mid - 1

        return answer

    first = find_first()

    if first == -1:
        return [-1, -1]

    last = find_last()

    return [first, last]


if __name__ == "__main__":
    p1 = [5, 7, 7, 8, 8, 8, 8, 10, 12, 12]
    print(solution(p1, 8))  # Output: [3, 6]

    p2 = [1, 2, 3, 4, 5]
    print(solution(p2, 3))  # Output: [2, 2]

    p3 = [1, 2, 3, 4, 5]
    print(solution(p3, 6))  # Output: [-1, -1]

    p4 = [7, 7, 7, 7]
    print(solution(p4, 7))  # Output: [0, 3]

# --------------------------------------------------------------------------------------
# Time Complexity: O(log n) + O(log n) = O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search - First and Last Occurrence
# --------------------------------------------------------------------------------------