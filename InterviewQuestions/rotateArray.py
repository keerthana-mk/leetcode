# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
class Solution:
    def rotate (self, nums: list[int], k: int) -> None:
        rotations=k % len(nums)
        return (nums[-rotations:]+nums[:-rotations])
s=Solution()
nums=[1,2,3,4,5,6,7]
print(s.rotate(nums,3))