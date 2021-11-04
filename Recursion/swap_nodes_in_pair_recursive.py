# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head=None

    def swapPairs(self, head):
        if(head != None and head.next != None):
            head.val,head.next.val = head.next.val,head.val
            self.swapPairs(head.next.next)
        print(head.val,head.next.val)

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.val)
            temp = temp.next


# Driver program
llist = Solution()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Linked list before calling pairWiseSwap() ")
llist.printList()



print("\nLinked list after calling pairWiseSwap()")
llist.printList()