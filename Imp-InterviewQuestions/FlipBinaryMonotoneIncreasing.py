# https://leetcode.com/problems/flip-string-to-monotone-increasing/
# Flip String to Monotone
#
# A binary string is monotone increasing if it consists of some number of 0's (possibly none), ' \
# followed by some number of 1's (also possibly none).
#
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
#
# Return the minimum number of flips to make s monotone increasing.
# Example 2:
#
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
# Example 3:
#
# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
from collections import Counter

import mpmath.libmp


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        flips = 0
        for i in s:
            if i == "1":
                ones += 1
            else:
                flips += 1
            flips = min(ones, flips)
            print("Flips,ones=", flips,ones)
        return flips


s = Solution()
s1 = "00011000"
print(s.minFlipsMonoIncr(s1))
