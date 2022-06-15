# https://leetcode.com/problems/contains-duplicate-iii/
# Given an integer array nums and two integers k and t, return true if there are two distinct indices
# i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3
# Output: true

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        map = {}
        for i in range(n):
            if nums[i] not in map:
                map[nums[i]] = []
            map[nums[i]].append(i)
            m = len(map[nums[i]])
            if m >= 2:
                if abs(map[nums[i]][m - 1] - map[nums[i]][m - 2]) <= k:
                    return True

        return False