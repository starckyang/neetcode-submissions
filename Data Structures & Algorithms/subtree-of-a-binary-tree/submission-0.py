# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        def isSameTree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val == node2.val:
                return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)
            else:
                return False

        def _isSubTree(root, subroot):
            if root is None:
                return False
            if isSameTree(root, subroot):
                return True
            else:
                return _isSubTree(root.left, subroot) or _isSubTree(root.right, subroot)
        
        return _isSubTree(root, subRoot)