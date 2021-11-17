# Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's '
# in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
# Return the sorted array.
#
# Example 1:
#
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        binary_arr=[]
        count_binary={}
        for i in range(len(arr)):
            # binary_arr.append(('0'*7+bin(arr[i])[2:])[-4:])
        print(sorted(arr,key=lambda x:(bin(x).count('1'),x)))



s=Solution()
array1=[0,1,2,3,4,5,6,7,8]
print(s.sortByBits(array1))

##dint work
# class Solution:
#     def sortByBits(self, arr: list[int]) -> list[int]:
#         binary_arr=[]
#         count_binary={}
#         for i in range(len(arr)):
#             binary_arr.append(bin(arr[i])[2:])
#         for i in range(len(binary_arr)):
#             count_binary[binary_arr[i]]=binary_arr[i].count('1')
#         # print("count_binary",count_binary.keys())
#         sorted_arr=sorted(count_binary.keys())
#         # print("sorted count binary=",sorted_arr)
#         sorted_arr=[int(i,2) for i in sorted_arr]
#         return sorted_arr