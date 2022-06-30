# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_words = {}
        window_len  = 0
        l = 0
        for  r in range(len(s)):
            if s[r] in unique_words:
                l = max(unique_words[s[r]],l)

            window_len = max(window_len, r-l+1)
            unique_words[s[r]] = r+1

        return window_len

s = Solution()
str = "abcabcbb"

str1 = "bbbbb"
print(s.lengthOfLongestSubstring(str1))


