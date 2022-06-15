# https://leetcode.com/problems/longest-palindromic-substring/
# Longest Palindromic Substring
#
# Given a string s, return the longest palindromic substring in s.
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

'''
The goal is to create all palindromes of even and odd lengths while keeping track of the longest palindrome seen so far.

To make a palindrome with an odd length, For lengthier palindromes, fix a centre and expand in both directions,
i.e. fix I (index) as the centre and two indices as i1 = i+1 and i2 = i-1. If i1 and i2 are equal, reduce i2 and raise i1 to get the maximum length.

Find the even-length palindrome using a similar method.
Take two indices, i1 = I and i2 = i-1, and compare characters at i1 and i2 to get the greatest length until all pairs of compared characters are identical.
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        low = 0
        high = 0
        start = 0
        maxlength = 1
        for i in range(1, len(s)):
            low = i - 1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1
            low += 1
            high -= 1
            if s[low] == s[high] and high - low + 1 > maxlength:
                start = low
                maxlength = high - low + 1
            # odd length of substrings
            low = i - 1
            high = i + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1
            low += 1
            high -= 1
            if s[low] == s[high] and high - low + 1 > maxlength:
                start = low
                maxlength = high - low + 1
        print("output=", s[start:start + maxlength], start, maxlength)
        return s[start:start + maxlength]


s = Solution()
s1 = "babad"
s2 = "cbbd"
print(s.longestPalindrome(s1))
print(s.longestPalindrome(s2))
