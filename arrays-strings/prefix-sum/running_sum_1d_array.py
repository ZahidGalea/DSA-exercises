"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
from typing import List


class Solution:
    def runningSum_v1(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(nums[i] + result[i - 1])
        return result

    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = nums[0]
        # Se coloca el primer valor, porque si no fallaria por indices, ya que se
        # tiene que sumar con el anterior siempre.
        # minimo parte por 1 la construccion del prefix array.
        for x in range(1, len(nums)):
            ans[x] = nums[x] + ans[x - 1]
        return ans


solution = Solution()
assert solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
assert solution.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
assert solution.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
