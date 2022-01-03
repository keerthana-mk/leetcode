# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        m = len(nums1)
        n = len(nums2)
        if m > n:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    result.append(nums1[i])
                    nums2.remove(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    result.append(nums2[i])
                    nums1.remove(nums2[i])

        return result


s = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
resultant = s.intersect(nums1, nums2)
print(resultant)
