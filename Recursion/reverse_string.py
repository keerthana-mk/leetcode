# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/
# Write a function that reverses a string. The input string is given as an array of characters s.
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.recursive_reverse(s, 0, len(s) - 1)
        return s

    def recursive_reverse(self, s, start, stop):
        if (start >= stop):
            return
        s[start], s[stop] = s[stop], s[start]
        self.recursive_reverse(s, start + 1, stop - 1)
        print(s)


if __name__ == '__main()__':
    S = ["h", "e", "l", "l", "o"]
    Solution.reverseString(S)
