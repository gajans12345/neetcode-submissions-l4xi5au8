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
        temp = []
        lst = []
        lst1 = []
        temp.append(p)
        while temp:
            v = temp.pop()
            if v is None:
                lst.append(None)
                continue
            lst.append(v.val)
            temp.append(v.right)
            temp.append(v.left)
        temp.append(q)
        while temp:
            v = temp.pop()
            if v is None:
                lst1.append(None)
                continue
            lst1.append(v.val)
            temp.append(v.right)
            temp.append(v.left)
        print(lst)
        print(lst1)
        if lst == lst1:
            return True
        else:
            return False