# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Kth Smallest Element in a BST
#
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
'''
Approach 1: Recursive Inorder Traversal
It's a very straightforward approach with O(N)O(N) time complexity. The idea is to build an inorder traversal of BST which is an array sorted in the ascending order. Now the answer is the k - 1th element of this array.

Approach 2: Iterative Inorder Traversal
The above recursion could be converted into iteration, with the help of stack. This way one could speed up the solution because there is no need to build the entire inorder traversal, and one could stop after the kth element.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []
        TreeNode node = root
        def inorder(root):
            if root:
                root = inorder(root.left)
                in_order.append(root.val)
                root = inorder(root.right)

        inorder(root)
        return in_order[k-1]