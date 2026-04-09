# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            temp = head.next
            temp.next = head
            head.next = None
            return temp
        t1= head
        t2 = head.next
        t3 = head.next.next
        head.next = None
        while t3 is not None:
            t2.next = t1
            t1 = t2
            t2 = t3
            t3 = t3.next
        t2.next = t1
        return t2
        