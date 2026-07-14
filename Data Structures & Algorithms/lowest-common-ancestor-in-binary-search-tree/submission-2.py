# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def child_scan(parent):
            if parent is None:
                return (None, False, False)
            (pa1, pc1, qc1), (pa2, pc2, qc2) = child_scan(parent.left), child_scan(parent.right)
            pc = (pc1 or pc2)
            qc = (qc1 or qc2)
            if pa1 or pa2:
                return (pa1, True, True) if pa1 else (pa2, True, True)
            if (pc and qc) or (pc and parent.val == q.val) or (qc and parent.val == p.val):
                return (parent, True, True)
            if parent.val == p.val:
                return (None, True, False)
            if parent.val == q.val:
                return (None, False, True)
            return (None, pc, qc)
        return child_scan(root)[0]
