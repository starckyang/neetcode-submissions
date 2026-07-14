# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def _balanced(root):
            if not root:
                return True, 0
            lbal, llength = _balanced(root.left)
            rbal, rlength = _balanced(root.right)
            if (lbal and rbal) and (-1<=(llength-rlength)<=1):
                return True, max(llength, rlength)+1
            return False, max(llength, rlength)+1

        return _balanced(root)[0]
