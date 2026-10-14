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
        q.append([root,level])
        temp[level] = [root.val]
        lst = []
        while q:
            curr = q.popleft()
            
            if curr[0].left:
                q.append([curr[0].left,curr[-1]+1])
                if curr[-1]+1 in temp:
                    temp[curr[-1]+1].append(curr[0].left.val)
                else:
                    temp[curr[-1]+1] = [curr[0].left.val]
            if curr[0].right:
                q.append([curr[0].right,curr[-1]+1])
                if curr[-1]+1 in temp:
                    temp[curr[-1]+1].append(curr[0].right.val)
                else:
                    temp[curr[-1]+1] = [curr[0].right.val]
        for key,value in temp.items():
            lst.append(value)
        return lst


        