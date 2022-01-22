# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)
        print(a, b)
        if a == b:
            return True
        else:
            return False


s1 = Solution()
s = "anagram"
t = "nagaram"
print(s1.isAnagram(s, t))
