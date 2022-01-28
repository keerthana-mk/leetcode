# Given an arr nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
# color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


class Solution:
    def sortColors (self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        n = len(nums) - 1
        self.quick_sort(0, n,nums)
        print(nums)

    def partition (self, start, end, arr):

        # Initializing pivot's index to start
        pivot_index = start
        pivot = arr[pivot_index]
        while start < end:
            while start < len(arr) and arr[start] <= pivot:
                start += 1

            while arr[end] > pivot:
                end -= 1
            if (start < end):
                arr[start], arr[end] = arr[end], arr[start]
        arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
        return end

    # The main function that implements QuickSort
    def quick_sort (self, start, end, arr):

        if (start < end):
            p = self.partition(start, end, arr)

            self.quick_sort(start, p - 1, arr)
            self.quick_sort(p + 1, end, arr)


s = Solution()
nums = [0, 2, 2, 2, 0, 2, 1, 1]
print(s.sortColors(nums))
