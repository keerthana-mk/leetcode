#https://leetcode.com/problems/contains-duplicate-iii/
#Given an integer array nums and two integers k and t, return true if there are two distinct indices
#i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
#Example 1:

#Input: nums = [1,2,3,1], k = 3, t = 0
#Output: true

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        n = len(nums)
        map = {}
        for i in range(n):
            if nums[i] not in map:
                map[nums[i]] = []
            map[nums[i]].append(i)

        uniqueNumbers = list(map.keys())
        m = len(uniqueNumbers)

        for x in uniqueNumbers:
            indicesList = map[x]
            for index in range(len(indicesList)-1):
                if abs(indicesList[index] - indicesList[index+1]) <= k:
                    return True
        uniqueNumbers.sort()
        for i in range(m):
            for j in range(i+1, m):
                firstNum, secondNum = uniqueNumbers[i], uniqueNumbers[j]
                if abs(firstNum - secondNum) <= t:
                    firstNumIndices, secondNumIndices = map[firstNum], map[secondNum]
                    for x in firstNumIndices:
                        for y in secondNumIndices:
                            if abs(x-y) <= k:
                                return True
                            else:
                                break
                else:
                    break
        return False