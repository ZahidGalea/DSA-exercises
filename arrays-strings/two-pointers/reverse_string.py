class Solution(object):
    def reverseString(self, s):
        point_1 = 0
        point_2 = len(s) - 1
        while point_1 < point_2:
            letter_a = s[point_1]
            letter_b = s[point_2]
            s[point_1] = letter_b
            s[point_2] = letter_a

            point_1 += 1
            point_2 -= 1

        print(s)