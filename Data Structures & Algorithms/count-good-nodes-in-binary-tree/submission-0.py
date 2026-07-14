# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        # dfs should be applied
        self.dfs(root)
        return self.good_nodes

    def dfs(self, node, p_max=-math.inf):
        if node is None:
            return
        if node.val >= p_max:
            self.good_nodes += 1
            p_max = node.val
        self.dfs(node.left, p_max), self.dfs(node.right, p_max)
        

