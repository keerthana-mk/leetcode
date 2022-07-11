# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
# Input: root = [1]
# Output: [[1]]
#
# Input: root = []
# Output: []


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return [[]]
        q = collections.deque()
        q.append(root.val)
        while q:
            val =[]
            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(val)
        return result
