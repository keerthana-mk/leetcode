# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        if len(strs) == 0:
            return [[""]]

        if len(strs) == 1:
            return [strs]

        dict = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word not in dict:
                dict[sorted_word] = [i]
            else:
                dict[sorted_word].append(i)

        print(dict)
        print(dict.values())
        return dict.values()

s =Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))