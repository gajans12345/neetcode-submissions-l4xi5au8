# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        stack = []
        temp = head

        # push all nodes to stack
        while temp is not None:
            stack.append(temp)
            temp = temp.next

        # pop to rebuild reversed list
        new_head = stack.pop()
        current = new_head

        while stack:
            node = stack.pop()
            current.next = node
            current = node

        current.next = None  # last node points to None

        return new_head


            
        