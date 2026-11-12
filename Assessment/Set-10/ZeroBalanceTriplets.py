# Category B | October DSA Exam | Practice Assessment | Set 10 | Problem 4: Zero Balance Triplets
# --------------------------------------------------------------------------------------
# Find all distinct triplets whose sum is zero.
# Each triplet must use three different positions.
# Print triplets in lexicographic order, or None.
# Constraints:
# 3 <= n <= 3000
# -10^5 <= value <= 10^5
# Use custom sorting.
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


def solution(arr):
    arr = merge_sort(arr)
    n = len(arr)
    result = []

    for i in range(n - 2):

        # Skip duplicate first values.
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i], arr[left], arr[right]])

                left += 1
                right -= 1

                # Skip duplicate second values.
                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                # Skip duplicate third values.
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result if result else None


if __name__ == "__main__":
    p1 = [-1, 0, 1, 2, -1, -4, 3, -2]
    print(solution(p1))
    # Output:
    # [
    #   [-4, 1, 3],
    #   [-2, -1, 3],
    #   [-2, 0, 2],
    #   [-1, -1, 2],
    #   [-1, 0, 1]
    # ]

    p2 = [1, 2, 3, 4]
    print(solution(p2))  # Output: None

    p3 = [0, 0, 0, 0]
    print(solution(p3))  # Output: [[0, 0, 0]]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n^2)
# Space Complexity: O(n) auxiliary, excluding recursion and output details
# Pattern: Custom Merge Sort + Two Pointers (3Sum)
# --------------------------------------------------------------------------------------