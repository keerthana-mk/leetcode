# https://leetcode.com/problems/maximum-units-on-a-truck/
# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
#
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
#
# Return the maximum total number of units that can be put on the truck.
# Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
# Output: 8
# Explanation: There are:
# - 1 box of the first type that contains 3 units.
# - 2 boxes of the second type that contain 2 units each.
# - 3 boxes of the third type that contain 1 unit each.
# You can take all the boxes of the first and second types, and one box of the third type.
# The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
'''
Approach 1:Brute Force O(n^2)
Algorithm

Initially, the truck is empty, hence the remaining truck capacity that must be filled would be equal to the truck size. Initialise variable remainingTruckSize to truckSize.

The truck will be filled with boxes one by one until it is not full. In every iteration, we must find a box with maximum units from the remaining box types. Let's use the method findMaxUnitBox that would return the index of a box type with maximum units given by maxUnitBoxIndex in the 2D array \text{boxTypes}boxTypes.

Once, we have the maxUnitBoxIndex, we could find the number of boxes that we could put in the truck as a minimum of remainingTruckSize and the number of boxes available of a given type. Calculate the total number of units and reduce the truck's remaining capacity based on the number of boxes put in the truck.

Also, we must mark the current box as used. One way of doing this would be to simply mark the number of units as -1. When findMaxUnitBox would indicate that all the boxes are already used and we must terminate.

The process of filling the truck with box types would continue until the truck is not full i.e remainingTruckSize is greater than 00.

Approach 2: Using sorting O(nlogn)

Algorithm

Initially, the truck is empty, hence the remaining truck capacity that must be filled would be equal to the truck size. Initialise variable remainingTruckSize to truckSize.

Sort the array boxTypes in decreasing order of a number of units.

Start picking up each box type from boxTypes array starting from 0^{th}0
th
  position. The number of boxes that can be put in the truck would be the minimum of remainingTruckSize and the number of boxes available of the given type. Calculate the total number of units and reduce the truck's remaining capacity based on the number of boxes put in the truck.

The process of filling the truck with box types would continue until the truck is not full i.e remainingTruckSize is greater than 00.

'''


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        print(boxTypes)
        result = 0
        for numBoxes, units in boxTypes:
            print("num_boxes*units=", numBoxes * units, "trucksize=", truckSize)
            if numBoxes < truckSize:
                truckSize -= numBoxes
                result += (numBoxes * units)

            else:
                result += (truckSize * units)
                break
        print(result)
        return result


s = Solution()
boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
s.maximumUnits(boxTypes, truckSize)
