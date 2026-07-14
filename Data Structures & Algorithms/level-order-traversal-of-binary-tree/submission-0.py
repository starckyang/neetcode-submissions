# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs should be applied
        res = []
        def bfs(node, layer):
            if node is None:
                return
            if (len(res)-1) < layer:
                res.append([node.val])
            else:
                res[layer].append(node.val)
            bfs(node.left, layer+1), bfs(node.right, layer+1)
            return
        bfs(root, 0)
        return res
            