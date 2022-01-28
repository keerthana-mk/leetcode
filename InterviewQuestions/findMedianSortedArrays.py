# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.


'''
Merge 2 sorted lists find the median
'''


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) < 0:
            return nums2.index(len(nums2) - 1 / 2)
        if len(nums2) < 0:
            return nums1.index(len(nums1) - 1 / 2)
        if len(nums1) < 0 or len(nums2) < 0:
            return

        merged_list = nums1[:len(nums1)] + nums2[:len(nums2)]
        merged_list.sort()
        middle_index = (len(merged_list) - 1) // 2
        if len(merged_list) % 2 == 0:
            # print(middle_index,merged_list[middle_index] + merged_list[middle_index + 1])
            return float(merged_list[middle_index] + merged_list[middle_index + 1]) / 2
        else:
            return float(merged_list[middle_index])


s = Solution()
nums1 = [1, 5]
nums2 = [3, 4]
print(s.findMedianSortedArrays(nums1, nums2))
