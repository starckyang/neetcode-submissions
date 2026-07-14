# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return True, -math.inf, math.inf
            (lv, lmax, lmin), (rv, rmax, rmin) = dfs(root.left), dfs(root.right)
            if (not lv) or (not rv) or (root.val <= lmax) or (root.val >= rmin):
                return False, None, None
            else:
                return True, max(rmax, root.val), min(lmin, root.val)

        return dfs(root)[0]

        
            