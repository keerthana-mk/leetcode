# https://leetcode.com/problems/symmetric-tree/
#
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        preorder_arr = []
        post_arr = []
        self.preorder(root.left, preorder_arr)
        self.postorder(root.right, post_arr)
        # print(preorder_arr)
        # print(post_arr)
        n = len(post_arr)
        for i in range(len(preorder_arr)):
            if preorder_arr[i] != post_arr[i]:
                return False

        return True

    def preorder(self, root, preorder_arr):
        if root is None:
            preorder_arr.append(-sys.maxsize)
            return
        preorder_arr.append(root.val)
        self.preorder(root.left, preorder_arr)
        self.preorder(root.right, preorder_arr)

    def postorder(self, root, post_arr):
        if root is None:
            post_arr.append(-sys.maxsize)
            return
        post_arr.append(root.val)
        self.postorder(root.right, post_arr)
        self.postorder(root.left, post_arr)


s = Solution()
