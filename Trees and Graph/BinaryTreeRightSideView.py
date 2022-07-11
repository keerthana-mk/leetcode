# https://leetcode.com/problems/binary-tree-right-side-view/
#
# Binary Tree Right Side View
#
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
# Input: root = [1,null,3]
# Output: [1,3]
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        right_side_result =[]
        if not root:
            return result
        q = collections.deque()
        q.append(root)
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
        for i in result:
            right_side_result.append(i.pop(len(i)-1))
        return right_side_result
