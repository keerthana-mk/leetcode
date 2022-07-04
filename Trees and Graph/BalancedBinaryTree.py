# https://leetcode.com/problems/balanced-binary-tree/
# Balanced Binary Tree
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
# Input: root = []
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False
        if self.height(node.left) - self.height(node.right) > 1
            return False
        return True

    def height(self, node):
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height,right_height) + 1