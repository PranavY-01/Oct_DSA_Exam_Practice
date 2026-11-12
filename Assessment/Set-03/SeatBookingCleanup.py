# Category B | October DSA Exam | Practice Assessment | Set 03 | Problem 5: Seat Booking Cleanup
# --------------------------------------------------------------------------------------
# Remove extra duplicates from a sorted array.
# Each distinct value may appear at most twice.
# Modify the original array and return the new length k.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= seatID[i] <= 10^9
# Array is sorted in non-decreasing order.
# No extra array for the final answer.
# --------------------------------------------------------------------------------------

def solution(arr):
    n = len(arr)

    if n <= 2:
        return n

    write = 2

    for read in range(2, n):

        if arr[read] != arr[write - 2]:
            arr[write] = arr[read]
            write += 1

    return write


if __name__ == "__main__":
    # Test cases
    p1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    k = solution(p1)
    print(k)                  # Output: 7
    print(p1[:k])             # Output: [1, 1, 2, 2, 3, 3, 4]

    p2 = [1, 1, 2, 2, 3]
    k = solution(p2)
    print(k)                  # Output: 5
    print(p2[:k])             # Output: [1, 1, 2, 2, 3]

    p3 = [5, 5, 5, 5, 5]
    k = solution(p3)
    print(k)                  # Output: 2
    print(p3[:k])             # Output: [5, 5]

    p4 = [1, 2, 3, 4]
    k = solution(p4)
    print(k)                  # Output: 4
    print(p4[:k])             # Output: [1, 2, 3, 4]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Two Pointers / In-place Duplicate Removal
# --------------------------------------------------------------------------------------