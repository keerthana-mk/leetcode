# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# # Definition for singly-linked list.
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # result_node = None
        # current_node = None
        # head1, head2 = l1[0], l2[0]
        # print(head1,head2)
        # while head1 != None and head2 != None:
        #     if result_node == None:
        #         result_node = ListNode(head1 +head2)
        #         current_node = result_node
        #     else:
        #         new_node = ListNode(head1.val+head2.val)
        #         current_node.next =new_node
        #         current_node = new_node
        #     head1 = head1.next
        #     head2 = head2.next
        # current_node.next = head2 if head1 is None else head1
        # return result_node
        carry, head = 0, l1
        while l1 or l2:
            if not l1.next and l2:
                l1.next, l2.next = l2.next, l1.next

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, l1.val = divmod(val1 + val2 + carry, 10)
            print(carry,l1.val)

            prev = l1
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry: prev.next = ListNode(carry)
        return head

s = Solution()
l1 = ListNode([9,9,9,9,9,9,9])
l2 = ListNode([9,9,9,9])
print(s.addTwoNumbers(l1,l2))