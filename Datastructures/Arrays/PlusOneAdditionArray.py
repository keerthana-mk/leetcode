# https://leetcode.com/problems/plus-one
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.
# Example 1:
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#
# Example 3:
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        len_n = len(digits)
        for i in range(len_n):
            n = len_n - i -1
            if digits[n] == 9:
                print("am i coming here")
                digits[n] = 0
            else:
                digits[n] +=1
                return digits
        return [1]+digits

digits = [1, 2, 3]
digits1 = [9]
print(s.plusOne(digits))
print(s.plusOne(digits1))
