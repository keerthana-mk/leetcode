# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
# Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
#
# For example if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
# Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.
#
# Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
#
# Example 1:
#
# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

