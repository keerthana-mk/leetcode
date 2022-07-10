# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Lowest Common Ancestor of a Binary Search Tree
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
#
# Input: root = [2,1], p = 2, q = 1
# Output: 2

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while True:
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
