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
        dict1 = {}
        while temp:
            if temp in dict1:
                return True
            else:
                dict1[temp] = 0            
            temp = temp.next
        return False