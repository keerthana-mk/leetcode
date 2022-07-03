# https://leetcode.com/problems/validate-binary-search-tree/
# Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# #
# Input: root = [2,1,3]
# Output: true
#
# Input: root = [5, 1, 4, null, null, 3, 6]
# Output: false
# Explanation: The root node's value is 5 but its right child' value is 4.

# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Definition for a binary tree node.

'''
Approach 1: Recursive Traversal with Valid Range

check at each node the following conditions:
1. node.right.val>node.val
2. node.left.val<node.val
    are valid

Approach 2: Using Inorder Traversal.
left --> root --> right
the inorder traversal should have always be in increasing order.
Maintain a prev variable to check at each node if next right node is greater than the prev node. If not return False.
'''
import math
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -math.inf
        return self.inorder(root)
    def inorder(self, root):

        if root is None:
            return True
        if not self.inorder(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        return self.inorder(root.right)



s= Solution()
root = [5, 1, 4, None, None, 3, 6]
s.isValidBST(root)