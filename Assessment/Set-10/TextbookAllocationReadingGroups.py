# Category B | October DSA Exam | Practice Assessment | Set 10 | Problem 5: Textbook Allocation Reading Groups
# --------------------------------------------------------------------------------------
# Divide n books into exactly m non-empty contiguous groups.
# Minimise the maximum pages assigned to any group.
# If m > n, return -1.
# Constraints:
# 1 <= n <= 10^5
# 1 <= m <= 10^5
# 1 <= pages <= 10^4
# Do not use built-in max() or sum().
# --------------------------------------------------------------------------------------

def can_allocate(pages, m, limit):
    groups = 1
    current_pages = 0

    for value in pages:
        if current_pages + value <= limit:
            current_pages += value
        else:
            groups += 1
            current_pages = value

            if groups > m:
                return False

    return True


def solution(pages, m):
    n = len(pages)

    if m > n:
        return -1

    # Lower bound = largest individual book.
    low = pages[0]

    # Upper bound = total pages.
    high = 0

    for value in pages:
        if value > low:
            low = value
        high += value

    answer = high

    while low <= high:
        mid = (low + high) // 2

        if can_allocate(pages, m, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


if __name__ == "__main__":
    p1 = [25, 46, 28, 49, 24, 20]
    print(solution(p1, 3))  # Output: 77

    p2 = [10, 20, 30, 40]
    print(solution(p2, 2))  # Output: 60

    p3 = [10, 20]
    print(solution(p3, 3))  # Output: -1

# --------------------------------------------------------------------------------------
# Time Complexity: O(n log S), S = total pages
# Space Complexity: O(1)
# Pattern: Binary Search on Answer + Greedy
# --------------------------------------------------------------------------------------