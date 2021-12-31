# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for l in range(0, len(nums) - 1):
            for k in range(l + 1, len(nums) - 1):
                if nums[k] + nums[l] == target:
                    return [l, k]


s = Solution()
result = s.twoSum(nums=[3, 2, 4], target=6)
print(s.twoSum(nums=[3, 2, 4], target=6))
