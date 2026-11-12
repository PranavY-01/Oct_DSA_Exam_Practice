# Category B | October DSA Exam | Practice Assessment | Set 03 | Problem 3: Out of Stock Items to the End
# --------------------------------------------------------------------------------------
# Move all zeroes to the end while preserving the relative order of non-zero values.
# Modify the original array without creating another array.
#
# Constraints:
# 1 <= n <= 10^5
# 0 <= count[i] <= 10^9
# --------------------------------------------------------------------------------------

def solution(arr):
    write = 0

    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1

    return arr


if __name__ == "__main__":
    # Test cases
    p1 = [0, 14, 0, 3, 7, 0, 0, 9, 5]
    print(solution(p1))     # Output: [14, 3, 7, 9, 5, 0, 0, 0, 0]

    p2 = [1, 2, 3, 4]
    print(solution(p2))     # Output: [1, 2, 3, 4]

    p3 = [0, 0, 0, 0]
    print(solution(p3))     # Output: [0, 0, 0, 0]

    p4 = [1, 0, 2, 0, 3]
    print(solution(p4))     # Output: [1, 2, 3, 0, 0]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Two Pointers / In-place Stable Compaction
# --------------------------------------------------------------------------------------
