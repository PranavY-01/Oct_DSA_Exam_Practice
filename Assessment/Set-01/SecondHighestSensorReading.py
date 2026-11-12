# Category B | October DSA Exam | Practice Assessment | Set 01 | Problem 3: Second Highest Sensor Reading
# --------------------------------------------------------------------------------------
# Find the second-largest DISTINCT value in the array.
# Return None if fewer than two distinct values exist.
#
# Constraints:
# 1 <= n <= 10^5
# -10^9 <= reading[i] <= 10^9
# Do not use built-in max(), min(), sum() or sorting.
# --------------------------------------------------------------------------------------

def solution(readings):
    largest = None
    second_largest = None

    for value in readings:
        if largest is None or value > largest:
            second_largest = largest
            largest = value

        elif value != largest:
            if second_largest is None or value > second_largest:
                second_largest = value

    return second_largest


if __name__ == "__main__":
    # Test cases
    p1 = [31, 28, 35, 35, 29, -4, 35, 28, 30]
    print(solution(p1))     # Output: 31

    p2 = [9, 9, 5]
    print(solution(p2))     # Output: 5

    p3 = [-5, -2, -10]
    print(solution(p3))     # Output: -5

    p4 = [7, 7, 7]
    print(solution(p4))     # Output: None

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Single Pass / Two-Variable Tracking
# --------------------------------------------------------------------------------------