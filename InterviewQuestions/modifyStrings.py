# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
#
# Return the final string after all the conversions (possibly zero) have been made.
# If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
# Example1:
#
# Input: s = "?zs"
# Output: "azs"
# Explanation: There
# are
# 25
# solutions
# for this problem.From "azs" to "yzs", all are valid.Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".

class Solution:
    def modifyString (self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                for c in "abc":
                    if (i == 0 or s[i - 1] != c) and (i + 1 == len(s) or s[i + 1] != c):
                        s[i] = c
                        break

        return "".join(s)


sol = Solution()
sol.modifyString("?zs")
