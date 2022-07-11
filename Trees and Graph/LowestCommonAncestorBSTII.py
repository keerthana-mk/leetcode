# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Lowest Common Ancestor of a Binary Search Tree
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.
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

class Solution:
    res = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q: return None

        def search(root, p, q):
            if not root: return False
            mid = left = right = False
            if root.val == p.val or root.val == q.val:
                mid = True

            left = search(root.left, p, q)
            right = search(root.right, p, q)
            if mid:
                if left or right:
                    self.res = root
            elif left and right:
                self.res = root
            return mid or left or right

        search(root, p, q)
        return self.res