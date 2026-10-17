# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# there is a bound
# lower bound is if r is parent if l passed down
# upper bound passed down if r and parent if l
# before oyu push check this and push with pass down stuff
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        if not root:
            return False
        stack.append([root,None,None])
        while stack:           
            curr = stack.pop()
            if curr[0].right:
                if curr[0].right.val > curr[0].val and (curr[2] is None or curr[0].right.val < curr[2]):
                    stack.append([curr[0].right,curr[0].val,curr[2]])
                else:
                    return False
            if curr[0].left:
               
                if curr[0].left.val < curr[0].val and (curr[1] is None or curr[0].left.val > curr[1]):
                    stack.append([curr[0].left,curr[1],curr[0].val])
                else:
                    return False
        return True
        