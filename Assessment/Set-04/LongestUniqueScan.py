# Category B | October DSA Exam | Practice Assessment | Set 04 | Problem 5: Longest Unique Scan Run
# --------------------------------------------------------------------------------------
# Find the length of the longest contiguous subarray
# containing only unique elements.
#
# Constraints:
# Elements may be repeated. The subarray must be contiguous.
# --------------------------------------------------------------------------------------

def solution(arr):
    last_seen = {}
    left = 0
    max_length = 0

    for right in range(len(arr)):
        value = arr[right]

        # If value was seen inside the current window,
        # move left beyond its previous occurrence.
        if value in last_seen and last_seen[value] >= left:
            left = last_seen[value] + 1

        # Update the most recent position.
        last_seen[value] = right

        # Calculate current window length.
        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length

    return max_length


if __name__ == "__main__":
    p1 = [1, 2, 3, 2, 4, 5]
    print(solution(p1))  # Output: 4

    p2 = [1, 2, 3, 4, 5]
    print(solution(p2))  # Output: 5

    p3 = [1, 1, 1, 1]
    print(solution(p3))  # Output: 1

    p4 = []
    print(solution(p4))  # Output: 0

# --------------------------------------------------------------------------------------
# Time Complexity: O(n) - Each element is processed once.
# Space Complexity: O(n) - Dictionary stores last-seen indices.
# Pattern: Variable-size Sliding Window + Hash Map
# --------------------------------------------------------------------------------------