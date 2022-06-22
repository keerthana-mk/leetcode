# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#
# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, height: list[int]) -> int:
        area = 0
        n = len(height)
        maxLeft =[0] * n
        maxRight = [0] * n
        minLeftRight = [0] * n
        maxLeft[0] = height[0]
        maxRight[n-1] = height[n-1]
        print("maxLeft, maxRight",maxLeft,maxRight)
        for i in range(1, len(height)):
            print(height[i])
            if height[i] > maxLeft[i-1]:
                maxLeft[i] = height[i]
            else:
                maxLeft[i] =  maxLeft[i-1]

            if height[n - i-1] > maxRight[n-i]:
                maxRight[n-i-1] = height[n - i -1]
            else:
                maxRight[n - i - 1] = maxRight[n-i]

        for i in range(n):
            minLeftRight[i] = min( maxRight[i], maxLeft[i])
            diff = minLeftRight[i] - height[i]
            if diff >0 :
                area += diff
        return area

s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height1 = [4,2,0,3,2,5]
print(s.trap(height))
print(s.trap(height1))
