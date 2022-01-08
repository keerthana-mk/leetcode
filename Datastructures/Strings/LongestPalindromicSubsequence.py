# https://leetcode.com/problems/longest-palindromic-subsequence/
# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
# Example 1:
#
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        left, right = 0, len(s)-1
        new_s=[]
        while left<right:
            del_left = s[:left]+s[left+1:]
            del_right = s[:right]+ s[right+1:]
            print(del_right,del_left)
            if del_right == del_right[::-1]:
                new_s.append(del_right)
            elif del_left ==del_left[::-1]:
                new_s.append(del_left)
            left+=1
            right-=1
        max_length=0
        result =''
        print(new_s)
        for i in new_s:
            if len(i)>max_length:
                max_length=len(i)
                result = i
        return len(result)

s= Solution()
s1 = "cbbd"
print(s.longestPalindromeSubseq(s1))