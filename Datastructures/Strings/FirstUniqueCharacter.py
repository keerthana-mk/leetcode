# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
# First Unique Character in a String
#
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 2:
#
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
#
# Input: s = "aabb"
# Output: -1
from collections import Counter
from operator import itemgetter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i in c:
            if c[i] ==1:
                return s.index(i)
        return -1

s = Solution()
s1 = "leetcode"
print(s.firstUniqChar(s1))
