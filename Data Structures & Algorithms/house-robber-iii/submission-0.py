# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dict1 = {}
        def helper(node):
            if not node.left and not node.right: # base case
                dict1[node] = node.val
                return
            if node is None:
                return
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            
            dict1[node] = max(dict1.get(node.left,0) + dict1.get(node.right,0),
                  node.val + dict1.get(getattr(node.left,'left',None),0)
                           + dict1.get(getattr(node.left,'right',None),0)
                           + dict1.get(getattr(node.right,'left',None),0)
            
                           + dict1.get(getattr(node.right,'right',None),0))
        helper(root)
        return dict1[root]



        