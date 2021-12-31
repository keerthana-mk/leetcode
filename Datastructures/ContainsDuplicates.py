# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if(len(nums)!=len(set(nums))):
            return True
        else:
            return False



s = Solution()
nums = [1, 2, 3, 1]
print(s.containsDuplicate(nums))
