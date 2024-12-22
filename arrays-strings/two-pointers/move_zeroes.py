"""

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""
from typing import List


class Solution:
    # Keeps a count of where zeros starts...
    def moveZeroesBest(self, nums: list[int]) -> None:
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for left in range(len(nums)):
            right = left + 1
            if nums[left] == 0:
                while right < len(nums):
                    if nums[right] != 0:
                        nums[left] = nums[right]
                        nums[right] = 0
                        left += 1
                    right += 1
        return nums


solution = Solution()
assert solution.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert solution.moveZeroes([0]) == [0]
assert solution.moveZeroes([0, 0, 1]) == [1, 0, 0]
assert solution.moveZeroes([1, 0]) == [1, 0]
