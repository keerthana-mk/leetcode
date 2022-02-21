# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/solution/
#
# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#
# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:
#
# horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
# verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.
#
# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4
# Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake
# has the maximum area.

'''
Algorithm

Sort both horizontalCuts and verticalCuts in ascending order.

Initialize a variable maxHeight as the larger of the top and bottom edge: maxHeight = max(horizontalCuts[0], h - horizontalCuts[horizontalCuts.length - 1]).

Iterate through horizontalCuts starting from index 1 (skip the 0th index since it represents the edge cut, which we accounted for in the previous step). At each iteration, 
find the height defined by the ith  cut and the nearest cut above, horizontalCuts[i] - horizontalCuts[i - 1]. Update maxHeight if necessary.

Initialize a variable maxWidth as the larger of the left and right edge: maxWidth = max(verticalCuts[0], w - verticalCuts[verticalCuts.length - 1]).

Iterate through verticalCuts starting from index 1. At each iteration, find the width defined by the i^{th}i 
th
  cut and the nearest cut to the left, verticalCuts[i] - verticalCuts[i - 1]. Update maxWidth if necessary.

Our maximum area is maxHeight * maxWidth. Don't forget the modulo 10^{9} + 7, and depending on what language you're using, be careful of overflow. Return the maximum area.
'''


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        modulo = pow(10,9) + 7
        maxHeight = max(horizontalCuts[0],h - horizontalCuts[len(horizontalCuts)-1])

        for i in range(1,len(horizontalCuts)):
            maxHeight = max(maxHeight, (horizontalCuts[i] - horizontalCuts[i-1]))
        maxWidth = max(verticalCuts[0],w - verticalCuts[len(verticalCuts)-1])
        for i in range(1,len(verticalCuts)):
            maxWidth =max(maxWidth,(verticalCuts[i] - verticalCuts[i-1]))

        return (maxWidth*maxHeight) % modulo

s = Solution()
h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]
print(s.maxArea(h,w, horizontalCuts, verticalCuts))
