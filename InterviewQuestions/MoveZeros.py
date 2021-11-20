# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
class Solution:
    def moveZeroes (self, nums: list[int]) -> None:
        new_index=0
        count_zero=0
        if len(nums)==1:
            return nums
        print(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                count_zero+=1
            if nums[i] != 0:
                nums[new_index]=nums[i]
                new_index+=1
        for i in range(count_zero):
            nums[new_index]=0
            new_index+=1
        return nums
s=Solution()
nums = [0,1,0,3,12]
print(s.moveZeroes(nums))



