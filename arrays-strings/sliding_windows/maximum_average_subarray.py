"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

My steps is:

* Tienen que ser subarrays de tamaño K.
    Es decir, si hay 10 y k es 2, hay minimo 5 subarrays.
* Por cada subarray de tamaño k. tengo que obtener solo
la media de cada uno
* retornar la media maxima encontrada.

con left en 0 y right en k

tomar la suma y la cantidad
sacar el average del window
incrementar el left en +1 post calculo.




"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int):
        current = sum(nums[0:k])
        ans = current / k
        n = len(nums)

        for right in range(k, n):
            current += nums[right]
            current -= nums[right - k]

            ans = max(ans, current / k)
        print(ans)
        return ans


def test_cases():
    # assert Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4) == 12.75000
    # assert Solution().findMaxAverage(nums=[5], k=1) == 5
    # assert Solution().findMaxAverage(nums=[3,3,4,3,0], k=3) == 3.33333
    assert Solution().findMaxAverage(nums=[0, 4, 0, 3, 2], k=1) == 4


test_cases()
