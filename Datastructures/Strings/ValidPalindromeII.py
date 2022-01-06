# https://leetcode.com/problems/valid-palindrome-ii/
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#
# Example 2:
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
# Example 3:
#
# Input: s = "abc"
# Output: false
# brute Force answer
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         if s == s[::-1] or str is None:
#             return True
#         for i in range(len(s)):
#             new_str = list(s)
#             new_str.pop(i)
#             # print("new str:",i,new_str)
#             pal_str = ''.join(new_str)
#             # print(pal_str)
#             if pal_str == pal_str[::-1]:
#                 return True
#         return False

class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.check(s, 0, len(s) - 1, False)

    def check(self, s, left, right, skipped):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif not skipped:
                return self.check(s, left, right - 1, True) or self.check(s, left + 1, right, True)
            else:
                return False

        return True


s = Solution()
s1 = "abca"
s2 = "cbbcc"
print(s.validPalindrome(s2))
