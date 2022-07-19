# https://leetcode.com/problems/house-robber-ii/
# House Robber II
#
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Input: nums = [1,2,3]
# Output: 3

'''
Solving Original House Robber Problem with Dynamic Programming

Trivial cases:

If there is one house, the answer is the value of that house.
If there are two houses, the answer is max(house1, house2).
If there are three houses, you can either pick the middle house or the sum of the first and the last house. Therefore, it boils down to max(house3 + house1, house2).
To make the example more illustrative, imagine two thieves (t1 and t2) coordinating a grand robbery. They are equipped with walkie-talkies to communicate the values of houses to each other.

Before entering any of the houses, both t1 and t2 have values of zero.

t1, enters the first house and record the value of the house. If that is the only house to rob, they can rob this house and be done with it.

If there is more than one house, t1 will leave a note of maximum value reaped until this point (which is just the value of the first house) and move to the next house while t2 moves into the house t1 was in. Now, t1 and t2 are going to communicate over the walkie-talkie to ask who has the most value. At this point, t2 will read the note left by t1 when the values are compared. If they have only two houses to rob, they would rob the house with the most value and be done with it.

If there are three houses, t1 will leave a note of the maximum value reaped until this point and move to the next house. Then t1 will compare the value of the sum of the current house and the house which t2 is in with the value of the house t1 was in. The maximum value between those two will be chosen and t2 will move into the house next to it.

If there are four houses, t1 will leave a note of the maximum value reaped until this point and move to the next house. Then t1 will compare the value of the sum of the current house and the house which t2 is in with the value of the house t1 was in. The maximum value between those two will be chosen and t2 will move into the house next to it.

This procedure is done over and over again as long as there are houses in nums. If t1 has reached to the end of nums, t1 should have reaped the maximum amount obtainable from houses in nums.
'''
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         n= len(nums)-1
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) < 3:
#             return max(nums[0],nums[1])
#         dp =[0 for i in range(len(nums)+1)]
#         dp2 = [0 for i in range(len(nums) + 1)]
#         dp[0] =0
#         dp[1] = nums[0]
#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-1] , nums[i-1]+dp[i-2])
#         dp2[0] = 0
#         dp2[1] = 0
#         for i in range(2, len(nums)):
#             dp2[i] = max(dp2[i-1] , nums[i-1]+dp2[i-2])
#         return max(dp2[n-1],dp[n])

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: list[int]) -> int:
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1

s = Solution()
nums = [2, 7, 9, 3, 1]
nums1 = [2, 1, 3]
print(s.rob(nums))
print(s.rob(nums1))