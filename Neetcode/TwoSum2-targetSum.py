# Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add
# up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.
# length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def twoSum (self, numbers: list[int], target: int) -> list[int]:
        left_index = 0
        right_index = len(numbers) - 1
        while left_index < right_index:
            if numbers[left_index] + numbers[right_index] == target:
                return [left_index + 1, right_index + 1]
            if numbers[left_index] + numbers[right_index] < target:
                left_index += 1
            else:
                right_index -= 1


s = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(s.twoSum(numbers, target))
