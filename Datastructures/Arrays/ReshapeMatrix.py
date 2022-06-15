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
        new_mat = []
        result = [0 for i in range(c) for _ in range(r)]
        print(result)

        for row in mat:
            for col in row:
                new_mat.append(col)
        if(len(new_mat)!= r*c):
            return mat
        print("new_mat",new_mat)
        for i in range(r):
            for j in range(c):
                result.append(new_mat.pop(0))
        # print(result)
        return result


s = Solution()
mat = [[1, 2], [3, 4]]
r = 2
c = 2
print(s.matrixReshape(mat, r, c))
