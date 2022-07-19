# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police
# Example 1:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        maxSum = 0
        a = nums[0]

        if len(nums) == 1:
            print("i am coming here")
            return a
        b = max(nums[0], nums[1])
        if len(nums) < 3:
            return b
        for i in range(2, len(nums)):
            maxSum = max(a + nums[i], b)
            a = b
            b = maxSum
        return maxSum

s = Solution()
nums = [2,7,9,3,1]
nums1 =[2,1,1,2]
print(s.rob(nums))
print(s.rob(nums1))
