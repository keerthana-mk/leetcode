# https://leetcode.com/explore/featured/card/dynamic-programming/631/strategy-for-solving-dp-problems/4147/
# Delete and Earn
#
# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
#
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.
#
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
#
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points
import collections


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:

        dict_nums = collections.defaultdict(int)
        max_number = 0
        for i in nums:
            dict_nums[i] += i
            max_number = max(i,max_number)
        maxSum =[0] *(max_number+1)
        maxSum[1] = dict_nums[1]
        for i in range(2,len(maxSum)):
            maxSum[i] = max(maxSum[i-1],maxSum[i-2]+dict_nums[i])
        print(maxSum)
        return maxSum[max_number]

s = Solution()
nums = [3,4,2,2]
print(s.deleteAndEarn(nums))


