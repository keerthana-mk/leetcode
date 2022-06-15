# https://leetcode.com/problems/range-addition/
#
# You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].
#
# You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation,
# you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.
#
# Return arr after applying all the updates.
#
# Example 1:
# Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# Output: [-2,0,3,5,3]

class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        new_array = [0] * length
        for start, end, inc in updates:
            # print (new_array,i)
            new_array[start] += inc
            if end + 1 < len(new_array):
                new_array[end + 1] -= inc
        for i in range(1, len(new_array)):
            new_array[i] = new_array[i] + new_array[i - 1]
            # new_array[i[0]:i[1] + 1] = [new_array[ele] + i[2] for ele in range(i[0], i[1] + 1)]

        # print(new_array)
        return new_array


s = Solution()
length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
print(s.getModifiedArray(length, updates))
