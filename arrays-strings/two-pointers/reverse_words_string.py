"""

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.



Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"


Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

"""


class Solution:
    def faster(self, s: str) -> str:
        return ' '.join(map(lambda word: word[::-1], s.split()))

    # Mine without split.
    # Split is On... I didn't know
    def reverseWords(self, s: str) -> str:
        s = s + " "
        left = 0
        ans = []
        n = len(s)
        for x in range(n):
            last = False
            if x == n - 1:
                last = True
            if s[x] == " " or x == n - 1:
                right = x
                while left < right:
                    ans.append(s[right - 1])
                    right -= 1
                if not last: ans.append(" ")
                left = x + 1
        return "".join(ans)


solution = Solution()
assert solution.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
