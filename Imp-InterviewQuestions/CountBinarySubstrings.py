# https://leetcode.com/problems/count-binary-substrings/
# Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and
# all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.
# Example 1:
#
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

'''
Approach #1: Group By Character [Accepted]
Intuition

We can convert the string s into an array groups that represents the length of same-character contiguous blocks within the string.
For example, if s = "110001111000000", then groups = [2, 3, 4, 6].

For every binary string of the form '0' * k + '1' * k or '1' * k + '0' * k, the middle of this string must occur between
two groups.

Let's try to count the number of valid binary strings between groups[i] and groups[i+1]. If we have groups[i] = 2,
groups[i+1] = 3, then it represents either "00111" or "11000". We clearly can make min(groups[i], groups[i+1])
valid binary strings within this string. Because the binary digits to the left or right of this string must change
at the boundary, our answer can never be larger.

Algorithm

Let's create groups as defined above. The first element of s belongs in it's own group.
From then on, each element either doesn't match the previous element, so that it starts a new group of size 1;
or it does match, so that the size of the most recent group increases by 1.

Afterwards, we will take the sum of min(groups[i-1], groups[i]).

'''


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        # Forming groups
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                groups.append(1)
            else:
                groups[-1] += 1
            print(i,groups,groups[-1])

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans


class Solution1:
    def countBinarySubstr(self, s: str) -> int:
        prev_count = 0
        current_count = 1
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_count += 1
            else:
                result += current_count if current_count < prev_count else prev_count
                prev_count = current_count
                current_count = 1
            if i == len(s) - 1:
                result += current_count if current_count < prev_count else prev_count
        return result


s1 = Solution()
s = "00110011"
print(s1.countBinarySubstrings(s))

s2 = Solution1()
# s = "00110011"
print("from solution2",s2.countBinarySubstr(s))
