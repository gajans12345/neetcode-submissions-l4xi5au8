class Solution:
    def lowestCommonAncestor(self, root, p, q):
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:   # both smaller, so go left
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val: # both bigger, so go right
                curr = curr.right
            else:                                       # split (or curr is p or q)
                return curr