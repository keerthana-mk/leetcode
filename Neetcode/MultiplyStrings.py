# https://leetcode.com/explore/featured/card/google/59/array-and-strings/3051/
# Multiply Strings
#
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"

class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:

         if "0" in [nums1, nums2]:
             return "0"

         result = [0] * (len(nums1) + len(nums2))
         nums1, nums2 = nums1[::-1],nums2[::-1]

         for i in range(len(nums1)):
             for j in range(len(nums2)):
                 digit = ((ord(nums1[i])-ord("0"))*(ord(nums2[j])-ord("0")))
                 result[i+j] += digit
                 result[i+j+1] += result[i+j] // 10
                 result[i+j] = result[i+j] % 10
         print(result)

         return self.converttoString(result)

    def converttoString(self, result):
        product = 0
        numsofzeros = 0
        for i in range(len(result)-1,-1,-1):
            product = product* 10 + (result[i])
        return str(product)


s = Solution()
num1 = "123"
num2 = "456"
print(s.multiply(num1, num2))