# https://leetcode.com/problems/valid-palindrome/
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = re.sub(r"[^A-Za-z0-9]+","",s).lower()

        print(s1)
        end = len(s1)
        for i in range(1,len(s1)):
            # print(s1[i-1],s1[len(s1)-i])
            if s1[i-1] == s1[len(s1)-i]:
                continue
            else:
                return False
        return True


s = Solution()
st = "A man, a plan, a canal: Panama"
print(s.isPalindrome(st))


