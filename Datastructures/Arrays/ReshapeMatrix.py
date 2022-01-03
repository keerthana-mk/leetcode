# https://leetcode.com/problems/reshape-the-matrix/
# In MATLAB, there is a handy function called reshape which can reshape an m x n
# matrix into a new one with a different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing the number
# of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
# Input: mat = [[1, 2], [3, 4]], r = 1, c = 4
# Output: [[1, 2, 3, 4]]

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows = mat[0]
        cols = mat
        new_mat = [j for i in mat[0] for j in i]
        print(new_mat)


s = Solution()
mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(s.matrixReshape(mat, r, c))
