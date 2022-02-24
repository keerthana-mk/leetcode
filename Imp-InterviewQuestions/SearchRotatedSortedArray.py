# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Search in Rotated Sorted Array
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4
#
# Example 2:
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# Output: -1

'''
Algorithm

As in the normal binary search, we keep two pointers (i.e. start and end) to track the search scope. At each iteration, we reduce the search scope into half, by moving either the start or end pointer to the middle (i.e. mid) of the previous search scope.

Here are the detailed breakdowns of the algorithm:

Initiate the pointer start to 0, and the pointer end to n - 1.

Perform standard binary search. While start <= end:

Take an index in the middle mid as a pivot.

If nums[mid] == target, the job is done, return mid.

Now there could be two situations:

Pivot element is larger than the first element in the array, i.e. the subarray from the first element to the pivot is non-rotated, as shown in the following graph.

Pivot element is smaller than the first element of the array, i.e. the rotation index is somewhere between 0 and mid. It implies that the sub-array from the pivot element to the last one is non-rotated, as shown in the following graph.

  - If the target is located in the non-rotated subarray:
  go right: `start = mid + 1`.

  - Otherwise: go left: `end = mid - 1`.
We're here because the target is not found. Return -1.
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low<= high:
            mid = low + (high - low) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[high]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                 if target <= nums[high] and target > nums[low]:
                        low = mid + 1
                 else:
                        high = mid -1
        return -1

# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         # print(nums)
#         min_element_index = nums.index(min(nums))
#         # print(min_element_index)
#         nums = nums[-min_element_index+1:] + nums[:-min_element_index+1]
#         # print("nums =",nums)
#         result = self.binarySearch(nums, target)
#         if result>=0:
#             return result
#         return -1
#
#     def binarySearch(self, nums, target):
#         low =0
#         high = len(nums)-1
#         # mid = low + (high) //2
#         # print(low, high,mid)
#         while low <= high:
#             mid = low + (high - low) // 2
#             if nums[mid] == target:
#                 return mid
#             elif target > nums[mid]:
#                 # print("I am here : target > nums[mid]")
#                 low = mid + 1
#                 # self.binarySearch(nums,mid + 1,high,target)
#                 # print("low = ", low)
#             elif target < nums[mid]:
#                 # print("I am here : target < nums[mid]")
#                 high = mid - 1
#                 # print("high =", high)
#                 # self.binarySearch(nums, low, mid-1, target)
#         return -1
s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 3
print(s.search(nums,target))
print(s.search(nums1, target1))