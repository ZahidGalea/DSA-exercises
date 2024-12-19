"""
Given an array of integers nums, you start with an initial positive value startValue.
** It can be 0, because even all can be plus and keep ahead 1.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
** so, Ill get my value and sum with each value... in resume the start value is my startValue.

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
** Increase startValue until there is not < 1 in any prefix sum.


if I make a prefix sum and in any case there is a min value - StartValue < 1:
then it should not ve valid...
best case is O(n)...

----

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:

Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive.
Example 3:

Input: nums = [1,-2,-3]
Output: 5

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100

"""
from typing import List


class Solution:
    def minStartValue_legacy(self, nums: List[int]) -> int:
        start_value = 0
        ans = 0
        while ans < 1:
            start_value += 1
            new_nums = nums.copy()
            new_nums[0] = start_value + nums[0]

            ans = new_nums[0]
            if ans < 1:
                continue
            for i in range(1, len(new_nums)):
                ans = new_nums[i] + ans
                if ans < 1:
                    break
        return start_value

    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        start_value = 1

        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i - 1]

        while True:
            if all([True if (x + start_value) >= 1 else False for x in prefix]):
                return start_value
            start_value += 1

    # Version inteligente:
    def minStartValue_better(self, nums: List[int]) -> int:
        p = []
        p.append(nums[0])
        # Memory efficient. hace appends al final de la cola
        for i in range(1, len(nums)):
            p.append(p[-1] + nums[i])

        # obtiene el valor minimo
        m = min(p)
        if m >= 0:
            # si en el prefix, no hay negativos, quiere decir que con el 1, ya es suficiente.
            return 1
        else:
            # resta cual es el valor necesario para que M, llegue a 1. xd
            return 1 - m


solution = Solution()
assert solution.minStartValue([-3, 2, -3, 4, 2]) == 5
assert solution.minStartValue([1, 2]) == 1
assert solution.minStartValue([1, -2, -3]) == 5
