# Category B | October DSA Exam | Practice Assessment | Set 04 | Problem 4: Plagiarism Pattern Scanner
# --------------------------------------------------------------------------------------
# Find all starting indices where a substring of s is an anagram of p.
# Include overlapping matches.
# Return None if no matching substring exists.
#
# Constraints:
# 1 <= len(s), len(p) <= 10^5
# Only lowercase English letters a-z.
# No Counter, sorted(), or slicing inside the loop.
# --------------------------------------------------------------------------------------

def solution(s, p):
    n = len(s)
    m = len(p)

    if m > n:
        return None

    target = [0] * 26
    window = [0] * 26

    for ch in p:
        target[ord(ch) - ord('a')] += 1

    for i in range(m):
        window[ord(s[i]) - ord('a')] += 1

    result = []

    if window == target:
        result.append(0)

    for i in range(m, n):
        incoming = ord(s[i]) - ord('a')
        outgoing = ord(s[i - m]) - ord('a')

        window[incoming] += 1
        window[outgoing] -= 1

        if window == target:
            result.append(i - m + 1)

    if len(result) == 0:
        return None

    return result


if __name__ == "__main__":
    # Test cases
    p1 = ("cbaebabacd", "abc")
    print(solution(*p1))     # Output: [0, 6]

    p2 = ("abab", "ab")
    print(solution(*p2))     # Output: [0, 1, 2]

    p3 = ("abcdef", "xyz")
    print(solution(*p3))     # Output: None

    p4 = ("aaaaaa", "aa")
    print(solution(*p4))     # Output: [0, 1, 2, 3, 4]

# --------------------------------------------------------------------------------------
# Time Complexity: O(26 * n), effectively O(n) for fixed alphabet
# Space Complexity: O(1), excluding output list
# Pattern: Fixed-Size Sliding Window / Frequency Counting
# --------------------------------------------------------------------------------------