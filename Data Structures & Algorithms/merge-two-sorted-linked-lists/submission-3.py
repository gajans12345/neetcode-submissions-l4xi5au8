# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        head = ListNode(0,None)
        curNode = None
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        if temp1.val >= temp2.val:
                head = ListNode(temp2.val)
                temp2 = temp2.next
        else:
            head = ListNode(temp1.val)
            temp1 = temp1.next
        curNode = head
        while temp1 is not None and temp2 is not None:
            print(temp1.val,temp2.val)
            if temp1.val >= temp2.val:
                curNode.next = ListNode(temp2.val)
                temp2 = temp2.next
                curNode = curNode.next
            else:
                curNode.next = ListNode(temp1.val)
                temp1 = temp1.next
                curNode = curNode.next
        if temp2 is None:
            v = temp1
            while v is not None:
                curNode.next = ListNode(v.val)
                curNode = curNode.next
                v = v.next


        elif temp1 is None:
            v = temp2
            while v is not None:
                curNode.next = ListNode(v.val)
                curNode = curNode.next
                v = v.next
        return head
            
            
