"""
You are given a 0-indexed array nums of n integers, and an integer k.

"The k-radius average for a subarray of nums centered at some index i with the radius k is":
the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.


an array, where each value, is the avg of a window of len k of a original array..
returns array.

i - k and i + k (inclusive)
if len(left) or len(right) < k, then -1.

round each value to floor.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

# init array in [-1] * nums
# -1 for arr[:k] and arr[-k:] as not necessary.


Example 1:


Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
- The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
  Using integer division, avg[3] = 37 / 7 = 5.
- For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
- For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
- avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
Example 2:

Input: nums = [100000], k = 0
Output: [100000]
Explanation:
- The sum of the subarray centered at index 0 with radius 0 is: 100000.
  avg[0] = 100000 / 1 = 100000.
Example 3:

Input: nums = [8], k = 100000
Output: [-1]
Explanation:
- avg[0] is -1 because there are less than k elements before and after index 0.


Constraints:

n == nums.length
1 <= n <= 105
0 <= nums[i], k <= 105

"""
from typing import List


class Solution:

    def bestSolution(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        windowSize = 2 * k + 1
        if k == 0:
            return nums
        if (windowSize > n):
            return avgs
        # To use sliding window, we need to first get sum of first window
        windowSum = sum(nums[:windowSize])
        avgs[k] = windowSum // windowSize  # adds avg on kth element because elements before k will be -1 or covered on cases defined above
        # Now iterate by sliding the window by each element
        for i in range(windowSize, n):
            windowSum = windowSum - nums[i - windowSize] + nums[i]
            avgs[i - k] = windowSum // windowSize  # i-k here to add avg from element next to kth
        return avgs

    # This works!
    # I can do it On, with a fixed window, summing and resting right and left.
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr = [-1] * n

        window_len = (k * 2) + 1
        if k == 0:
            return nums

        if window_len > n:
            return arr

        # Esto no es necesario, ver el de arriba.
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])

        arr[k] = int(prefix[k * 2] / window_len)
        for i in range(k + 1, n - k):
            arr[i] = int((prefix[i + k] - prefix[i - (k + 1)]) / window_len)

        return arr

    # First worst solution n2
    def getAverages_first_attemp(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr = [-1] * len(nums)
        if k > n:
            return arr

        # only for valid nums to calculate:
        for i in range(k, n - k):
            arr[i] = int(sum(nums[i - k:i + k + 1]) / ((k * 2) + 1))

        print(arr)
        return arr


x = sum([40527, 53696, 10730, 66491, 62141]) / 5
print(x)
x = sum([53696, 10730, 66491, 62141, 83909]) / 5
print(x)
solution = Solution()
assert solution.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3) == [-1, -1, -1, 5, 4, 4, -1, -1, -1]
assert solution.getAverages([100000], 0) == [100000]
assert solution.getAverages([8], 100000) == [-1]
assert solution.getAverages([40527, 53696, 10730, 66491, 62141, 83909, 78635, 18560], 2) == [-1, -1, 46717, 55393,
                                                                                             60381, 61947, -1, -1]
