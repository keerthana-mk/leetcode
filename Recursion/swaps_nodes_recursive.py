# Definition for singly-linked list.
# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head  or not head.next :
            return head
        Head1 = head
        Head2 = head.next
        temp =  self.swapPairs(Head2.next)
        Head2.next = Head1
        Head1.next = temp
        # print(Head1,Head2)
        return Head2






        
