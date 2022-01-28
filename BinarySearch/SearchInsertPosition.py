# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
# Example
# 1:
#
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
#
# Example
# 2:
#
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low=0
        high= len(nums)-1
        while low<= high:
            mid= low+(high-low)//2
            # print("mid",mid)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return low


s=Solution()
nums=[1, 3, 5, 6]
print(s.searchInsert(nums,2))