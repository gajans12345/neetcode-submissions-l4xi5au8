# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# as you traverse pass down a max
# then essentially, if it is geater then add o some list or smtng
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        if not root:
            return 0
        def helper(node,currMax):
            nonlocal counter
            if node.val >= currMax:
                counter+=1
            maxCal = max(currMax,node.val)
            if node.left:
                helper(node.left,maxCal)
            if node.right:
                helper(node.right,maxCal)
            if not node.left and not node.right:
                return
        helper(root,root.val)
        return counter

        