# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            t1 = head
            t2 = head.next
            t1.next = None
            while t2.next is not None:
                t3 = t2.next
                t2.next = t1
                t1 = t2
                t2 = t3
        t2.next = t1
        return t2
        

       