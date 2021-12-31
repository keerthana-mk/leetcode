# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police
# Example 1:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
class Solution:
    def rob (self, nums: list[int]) -> int:
        sum_total_even = 0
        sum_total_odd=0
        # if len(nums)==2:
        #     return max(nums[1],nums[0])
        for i in range(0, len(nums), 2):
            sum_total_even += (nums[i])
        for i in range(1, len(nums),2):
            sum_total_odd+=nums[i]
        if sum_total_even > sum_total_odd:
            return sum_total_even
        else:
            return sum_total_odd

s = Solution()
nums = [2,7,9,3,1]
print(s.rob(nums))
