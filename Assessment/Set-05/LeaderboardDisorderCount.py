# Category B | October DSA Exam | Practice Assessment | Set 05 | Problem 4: Leaderboard Disorder Count
# --------------------------------------------------------------------------------------
# Count inversions using Merge Sort.
# An inversion is a pair (i, j) where i < j and arr[i] > arr[j].
#
# Constraints:
# 1 <= n <= 10^5
# 0 <= scores[i] <= 10^9
# Built-in sorting is prohibited.
# --------------------------------------------------------------------------------------

def solution(arr):

    def merge_sort(left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        count = merge_sort(left, mid)
        count += merge_sort(mid + 1, right)

        # Merge both sorted halves.
        temp = []
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])

                # All remaining left-half elements
                # form inversions with arr[j].
                count += mid - i + 1
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        # Copy merged elements back into original array.
        for k in range(len(temp)):
            arr[left + k] = temp[k]

        return count

    if not arr:
        return 0

    return merge_sort(0, len(arr) - 1)


if __name__ == "__main__":
    p1 = [5, 3, 8, 6, 2, 7]
    print(solution(p1))  # Output: 7

    p2 = [1, 2, 3, 4]
    print(solution(p2))  # Output: 0

    p3 = [4, 3, 2, 1]
    print(solution(p3))  # Output: 6

    p4 = [2, 2, 1]
    print(solution(p4))  # Output: 2

# --------------------------------------------------------------------------------------
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Pattern: Divide and Conquer + Merge Sort + Inversion Counting
# --------------------------------------------------------------------------------------