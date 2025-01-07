"""

Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.


Constraints:

1 <= arr.length <= 1000
0 <= arr[i] <= 1000
"""

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        n = set(arr)
        return len([x for x in arr if x + 1 in n])

    # Less memory using a counter
    def countElements(self, arr: List[int]) -> int:
        counter = 0
        check = set(arr)

        for i in range(len(arr)):
            if arr[i] + 1 in check:
                counter += 1

        return counter


solution = Solution()
assert solution.countElements([1, 2, 3]) == 2
assert solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]) == 0
assert solution.countElements([1, 1, 2, 2]) == 2
