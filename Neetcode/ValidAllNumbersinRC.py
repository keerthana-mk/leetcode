# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
# Check if Every Row and Column Contains All Numbers
#
# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
#
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
#
# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.
#
# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
# Hence, we return false.
import collections
class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] in rows[r] or matrix[r][c] in cols[c]:
                    return False

                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
        return True

s = Solution()
matrix = [[1, 1, 1], [1, 2, 3], [1, 2, 3]]
print(s.checkValid(matrix))