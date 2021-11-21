# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1:
#
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#

class Solution:
    def reverseWords (self, s: str) -> str:
        # reverseword = ""
        # words=s.split()
        # for word in words:
        #     word = word[::-1]
        #     reverseword = reverseword + word + " "
        # return reverseword
        return ' '.join(w[::-1] for w in s.split())


s=Solution()
s1 = "Let's take LeetCode contest"
print(s.reverseWords(s1))
