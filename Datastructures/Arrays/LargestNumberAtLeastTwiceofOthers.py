# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/discuss/1745503/Python-simple-solution-or-2-steps
# You are given an integer array nums where the largest integer is unique.
#
# Determine whether the largest element in the array is at least twice as much as
# every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
#
# Example 1:
#
# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_num = max(nums)
        for i, num in enumerate(nums):
            if i != nums.index(max_num) and num*2 > max_num:
                return -1
        return nums.index(max_num)
s=Solution()
nums = [3,6,1,0]
print(s.dominantIndex(nums))