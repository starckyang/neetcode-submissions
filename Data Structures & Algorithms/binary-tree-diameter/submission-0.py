# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # return length and distance
        def dfs(root):
            if root:
                ll, ld = dfs(root.left)
                rl, rd = dfs(root.right)
                return max(ll, rl)+1, max(ld, rd, ll+rl)
            return 0, 0

        return dfs(root)[1]