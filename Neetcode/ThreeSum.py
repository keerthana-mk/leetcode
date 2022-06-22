# https://leetcode.com/problems/3sum/
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = []
# Output: []
#
# Example 3:
# Input: nums = [0]
# Output: []

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         #brute force with 3 for loops -> O(n^3)
#         result = []
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] +nums[j] +nums[k] ==0:
#                             result.append([nums[i], nums[j], nums[k]])
#
#         return result


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        # if sum(nums) ==0:
        #     return result
        nums.sort()
        print(nums)
        for i , a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            left = i+1
            right = len(nums) -1
            # print(left, right)
            while left < right:
                if a + nums[left] + nums[right] > 0:
                    right -= 1
                elif a + nums[left] + nums[right] < 0:
                    left +=1
                else:
                    result.append([a, nums[left], nums[right]])
            # handle duplicate combinations
                    left +=1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return result


s = Solution()
nums =[-1,0,1,2,-1,-4]
nums1 = [0,0,0,0]
print(s.threeSum(nums))
print(s.threeSum(nums1))