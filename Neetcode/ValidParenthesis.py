# https://leetcode.com/problems/valid-parentheses/
# Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Input: s = "()[]{}"
# Output: true
#
# Input: s = "(]"
# Output: false


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets ={
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for i in s:
            if i in brackets:
                print(i)
                if stack and stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                print("I am here",i)
            print(stack)
        return True if not stack else False

s= Solution()
s1 = "()[{}[]]"
s2 = "(]()"
print(s.isValid(s1))
print(s.isValid(s2))
