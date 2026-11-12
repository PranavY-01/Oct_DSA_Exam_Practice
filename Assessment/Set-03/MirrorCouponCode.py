# Category B | October DSA Exam | Practice Assessment | Set 03 | Problem 1: Mirror Coupon Code
# --------------------------------------------------------------------------------------
# Check whether a phrase is a palindrome after ignoring non-alphanumeric characters
# and treating uppercase and lowercase letters as equal.
#
# Constraints:
# 1 <= length <= 2 * 10^5
# Printable ASCII characters
# No slicing reversal or reversed().
# --------------------------------------------------------------------------------------

def solution(s):
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return "NO"

        left += 1
        right -= 1

    return "YES"


if __name__ == "__main__":
    # Test cases
    p1 = "Was it a car or a cat I saw?"
    print(solution(p1))     # Output: YES

    p2 = "race a car"
    print(solution(p2))     # Output: NO

    p3 = ".,!@#"
    print(solution(p3))     # Output: YES

    p4 = "A man, a plan, a canal: Panama"
    print(solution(p4))     # Output: YES

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Two Pointers / Palindrome Validation
# --------------------------------------------------------------------------------------