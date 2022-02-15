# https://leetcode.com/problems/sliding-window-maximum/
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the max sliding window.
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n= len(nums)
        if n == 0:
            return []
        if len(nums) ==1:
            return nums
        left,right = [0] *n,[0]*n
        left [0] = nums[0]
        right[n-1] = nums[n-1]
        for i in range(1,n):
            if i % k ==0:
                left[i] = nums[i]
            else:
                left [i] = max(left[i-1],nums[i])

            j = n-i -1
            if j % k ==0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1],nums[j])
        # print("left = ",left)
        # print("right = ", right)
        result =[]
        for i in range(k-1,n):
            result.append(max(left[i],right[i-k+1]))
            # print(i,i-k+1,result)
        return result
        # q = deque() # decreasing queue
        #
        # for i in range(len(nums)):
        #     if q and q[-1] < q[nums[i]]:
        #         q.pop()
        #     q.append(i)
s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(s.maxSlidingWindow(nums, k))