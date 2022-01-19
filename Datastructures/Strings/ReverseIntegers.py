# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, n: int) -> int:
        # print("Am i coming here")

        if n > pow(2, 31) - 1 or n < pow(2, 31) * -1:
            return 0
        neg_flag = 0

        if n < 0:
            neg_flag = 1
            n *= -1
        rev = 0
        while n != 0:
            d = n % 10
            rev = rev * 10 + d
            n = n // 10

        if neg_flag:
            if rev > pow(2, 31) - 1 or rev < pow(2, 31) * -1:
                return 0
            else:
                return rev * -1
        else:
            if rev > pow(2, 31) - 1 or rev < pow(2, 31) * -1:
                return 0
            else:
                return rev


s = Solution()
n = -123
print("heelo", s.reverse1(n))
