# https://leetcode.com/problems/palindromic-substrings/
# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
# Example 2:
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        alist = [s[i:j + 1] for i in range(n) for j in range(i, n)]
        # print(alist)
        for i in alist:
            if i == i[::-1]:
                count += 1
        return count

s = Solution()
print(s.countSubstrings("aaa"))
