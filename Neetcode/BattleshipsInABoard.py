# https://leetcode.com/problems/battleships-in-a-board/
#
# Battleships in a Board
#
# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
#
# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column),
# where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
#
# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2
#
# Input: board = [["."]]
# Output: 0

class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        count = 0
        if len(board) == 0:
            return 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] =='.':
                    continue
                if i>0 and board[i-1][j] =='X':
                    continue
                if j>0 and board[i][j-1] =='X':
                    continue

                count+=1
        return count

s = Solution()
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(s.countBattleships(board))