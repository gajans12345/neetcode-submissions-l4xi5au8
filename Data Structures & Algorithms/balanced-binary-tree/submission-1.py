# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#HB is if height of left subtree and righ subtree differ by one
# repeat this procedure for every subtree
# recursive, pasisng info up, whihc is some count of the height and check
# at each node you have height of left and right subtree. compare
# you will return the height of that node
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        notBalanced = False
        def helper(node):
            nonlocal notBalanced
            if not node.left and not node.right:
                return 1
            if node.left:
                left = helper(node.left)
            else:
                left = 0
            if node.right:
                right = helper(node.right)
            else:
                right = 0
            #print(left,right,node.val)
            if abs(left - right) > 1:
                notBalanced = True
            return 1 + max(left,right)

            
            
        if root is None:
            return True
        else:
            helper(root)
        return not notBalanced
        