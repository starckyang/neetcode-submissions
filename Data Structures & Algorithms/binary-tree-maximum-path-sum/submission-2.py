# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def path_sum(node):
            if node is None:
                return 0, None
            (lsp, lt), (rsp, rt) = path_sum(node.left), path_sum(node.right)
            lt = -math.inf if lt is None else lt
            rt = -math.inf if rt is None else rt
            return (max(max(lsp, rsp, 0)+node.val, 0)), (max((lsp + rsp + node.val), max(lt, rt)))

        return path_sum(root)[1]