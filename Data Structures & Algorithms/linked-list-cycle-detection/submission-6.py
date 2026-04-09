class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        a = head
        b = head
        
        while b is not None and b.next is not None:
            a = a.next
            b = b.next.next
            
            if a == b:
                return True
        
        return False