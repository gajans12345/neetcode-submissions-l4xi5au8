# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        temp = p
        temp1 = q
        stack1 = []
        stack1.append(p)
        stack2 = []
        stack2.append(q)
        while stack1 or stack2:
            a = stack1.pop()
            b = stack2.pop()
            if a.val != b.val:
                return False
            if a.left and b.left:
                stack1.append(a.left)
                stack2.append(b.left)
            else:
                if a.left or b.left:
                    return False
            if a.right and b.right:
                stack1.append(a.right)
                stack2.append(b.right)
            else:
                if a.right or b.right:
                    return False
        return True
            
            

        
        