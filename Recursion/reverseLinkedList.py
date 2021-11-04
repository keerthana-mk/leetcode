# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/2378/
# Definition for singly-linked list.
# Given the head of a singly linked list, reverse the list, and return the reversed list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return rest
