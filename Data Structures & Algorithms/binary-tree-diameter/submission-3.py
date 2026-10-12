class Solution:
    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.maxC = max(self.maxC, left + right)   # bend at this node
        return 1 + max(left, right)                # depth for the parent

    def diameterOfBinaryTree(self, root):
        self.maxC = 0
        self.helper(root)
        return self.maxC