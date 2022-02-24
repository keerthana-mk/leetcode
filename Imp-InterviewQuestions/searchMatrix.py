# https://leetcode.com/problems/search-a-2d-matrix-ii/
#
# Search a 2D Matrix II
#
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
#
# Example2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false

'''
Solution

This question is actually quite a bit simpler than it might first seem.

No need for Binary Search!

Instead, since each row and column is sorted in ascending order, we can take advantage of an invariant.

Let’s say we are currently looking at position (r, c) in our matrix.

All the elements in row r that are to the left will be less than the element at (r, c).

All the elements in column c that are in later rows will be greater than the element at (r, c).

Therefore, we can start our search at the right-most element in the first row.

If the current element is greater than our target, then we decrement the column.

If the current element is less than our target, then we increment the row.

If the current element is equivalent to our target, then we can return True.

If our (r, c) exceeds the matrix bounds, then we can return False.

'''


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        if len(matrix) == 0:
            return False
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


s = Solution()
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
matrix1 = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target1 = 20
print(s.searchMatrix(matrix, target))
print(s.searchMatrix(matrix1, target1))