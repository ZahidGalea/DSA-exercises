from typing import List


class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        left = 0
        right = len(arr) - 1
        result = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            if abs(arr[left]) < abs(arr[right]):
                to_square = arr[right]
                right -= 1
            else:
                to_square = arr[left]
                left += 1
            result[i] = to_square ** 2

        return result
