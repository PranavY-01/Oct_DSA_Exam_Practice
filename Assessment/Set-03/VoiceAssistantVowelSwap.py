# Category B | October DSA Exam | Practice Assessment | Set 03 | Problem 2: Voice Assistant Vowel Swap
# --------------------------------------------------------------------------------------
# Reverse the order of vowels while preserving all other character positions.
# Vowels retain their original case.
#
# Constraints:
# 1 <= length <= 2 * 10^5
# English letters and spaces
# --------------------------------------------------------------------------------------

def solution(s):
    vowels = set("aeiouAEIOU")
    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:

        while left < right and chars[left] not in vowels:
            left += 1

        while left < right and chars[right] not in vowels:
            right -= 1

        if left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)


if __name__ == "__main__":
    # Test cases
    p1 = "Campus Library"
    print(solution(p1))     # Output: Campis Lubrary

    p2 = "hello"
    print(solution(p2))     # Output: holle

    p3 = "leetcode"
    print(solution(p3))     # Output: leotcede

    p4 = "AEIOU"
    print(solution(p4))     # Output: UOIEA

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pattern: Two Pointers / Character Filtering
# -------------------------------------------------------------------------------------- 