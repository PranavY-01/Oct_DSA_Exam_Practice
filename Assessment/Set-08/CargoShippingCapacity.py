# Category B | October DSA Exam | Practice Assessment | Set 08 | Problem 5: Cargo Shipping Capacity
# --------------------------------------------------------------------------------------
# Find the minimum ship capacity needed to ship all packages
# in order within at most D days.
#
# Constraints:
# 1 <= D <= n <= 5 * 10^4
# 1 <= weight[i] <= 500
# No built-in max() or sum().
# --------------------------------------------------------------------------------------

def solution(weights, D):

    # Calculate binary search boundaries manually.
    lo = 0
    hi = 0

    for weight in weights:
        if weight > lo:
            lo = weight

        hi += weight

    answer = hi

    # Check whether a given capacity is feasible.
    def can_ship(capacity):
        days = 1
        current_load = 0

        for weight in weights:

            if current_load + weight <= capacity:
                current_load += weight

            else:
                days += 1
                current_load = weight

        return days <= D

    # Binary search for minimum feasible capacity.
    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if can_ship(mid):
            answer = mid
            hi = mid - 1

        else:
            lo = mid + 1

    return answer


if __name__ == "__main__":
    p1 = [4, 2, 7, 1, 8, 3, 5]
    print(solution(p1, 3))  # Output: 13

    p2 = [1, 2, 3, 4, 5]
    print(solution(p2, 1))  # Output: 15

    p3 = [1, 2, 3, 4, 5]
    print(solution(p3, 5))  # Output: 5

    p4 = [3, 2, 2, 4, 1, 4]
    print(solution(p4, 3))  # Output: 6

# --------------------------------------------------------------------------------------
# Time Complexity: O(n * log(sum(weights)))
# Space Complexity: O(1)
# Pattern: Binary Search on Answer + Greedy Feasibility Check
# --------------------------------------------------------------------------------------