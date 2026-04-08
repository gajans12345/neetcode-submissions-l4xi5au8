# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        temp = head
        if head.next is None:
            return False
        t2 = head.next
        while temp:
            if temp == t2:
                return True
            temp = temp.next
            if t2 and t2.next and t2.next.next:
                t2 = t2.next.next
            else:
                return False
        return False