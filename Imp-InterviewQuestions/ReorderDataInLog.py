# https://leetcode.com/problems/reorder-data-in-log-files/
# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
#
# There are two types of logs:
#
# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
#
# Reorder these logs so that:
#
# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.
#
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digits = []
        letters = []
        for i in logs:
            if i.split(" ")[1].isdigit():
                digits.append(i)
            elif i.split(" ")[1].isalpha():
                letters.append(i)
        # print("Digits = ", digits, " letters= ", letters)
        letters.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        return letters + digits


s = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(s.reorderLogFiles(logs))
