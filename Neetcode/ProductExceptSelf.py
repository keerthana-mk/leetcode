# https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


#brute force solution
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         result =[]
#         prefix = 1
#         suffix = 1
#         for i in range(len(nums)):
#             prefix = 1
#             suffix = 1
#             for j in range(0,i):
#                 prefix *= nums[j]
#             for k in range(i+1, len(nums)):
#                 suffix *= nums[k]
#             result.append(prefix*suffix)
#         return result

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1

        result =[1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        print("result after prefix =",result)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


s = Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))