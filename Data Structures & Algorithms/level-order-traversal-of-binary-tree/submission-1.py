# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # first sol is basically have an array hold each element and its level
        q = deque()
        temp = {}
        level = 1
        if not root:
            return []
        q.append(root)
        lst = []
        while q:
            temp = []
            v = len(q)
            for i in range(v):
                temp.append(q[0].val)
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            lst.append(temp)
        return lst


        