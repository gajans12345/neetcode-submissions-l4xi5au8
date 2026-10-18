class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def helper(root, p, q):  # are both p and q in this subtree?
            if not root:
                return False
            count = 0
            stack = [root]
            while stack:
                curr = stack.pop()
                if curr.val == p.val or curr.val == q.val:
                    count += 1
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            return count == 2

        if not root:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)   # check deeper first
        if left:
            return left
        right = self.lowestCommonAncestor(root.right, p, q)
        if right:
            return right

        if helper(root, p, q):   # nothing deeper works, so check this node
            return root
        return None