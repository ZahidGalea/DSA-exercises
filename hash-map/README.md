# Hash Map

A hash map is a data structure that stores key-value pairs with O(1) time complexity for basic operations.

## Key Operations & Time Complexity

- Add element: O(1)
- Remove element: O(1)
- Update value: O(1)
- Check if key exists: O(1)
- Find length: O(1)

## Advantages

- Fast operations (constant time)
- Flexible key types
- Direct access to values
- Useful for caching and counting

## Disadvantages®

- Higher memory usage
- Performance overhead for small datasets
- Expensive resizing operations
- Potential for collisions®

## Collisions

Collisions occur when different keys hash to the same value. Common solution:

- Chaining: Store multiple key-value pairs in linked lists at each array position

## Related: Sets

- Similar to hash maps but only store keys (no values)
- Used when only existence checking is needed
- All operations are O(1)
- Duplicates are automatically handled (only stored once)çççÇÇÇ 

## Counting Elements with Hash Maps

Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

```python
from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans
```

Example 2: 2248. Intersection of Multiple Arrays

Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

```python
from collections import defaultdict

def intersection(nums):
    counts = defaultdict(int)
    for arr in nums:
        for num in arr:
            counts[num] += 1
    
    ans = []
    for num, count in counts.items():
        if count == len(nums):
            ans.append(num)
    
    return ans
```

Example 3: 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.

```python
from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        frequencies = counts.values()
        return len(set(frequencies)) == 1
```
```python
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
```

Example 4: 560. Subarray Sum Equals K

Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
    
        return ans
```

Example 5: 1248. Count Number of Nice Subarrays

Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. The subarrays with 3 odd numbers in them are [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].

```python
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        
        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans
```
