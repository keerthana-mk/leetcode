# https://leetcode.com/problems/valid-palindrome/
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
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
        if s is None:
            return True
        str = re.sub('[^A-Za-z0-9]+', '', s).lower()
        print(str)
        print(str[::-1])
        if str[::-1] == str:
            return True
        else:
            return False


s=Solution()
s1 = "A man, a plan, a canal: Panama"
print(s.isPalindrome(s1))