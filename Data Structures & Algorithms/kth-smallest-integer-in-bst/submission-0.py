# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def order_search(root, count=0):
            if root is None:
                return None, 0
            if root.left:
                tar_val, count = order_search(root.left, count)
                if tar_val:
                    return tar_val, count
            count += 1
            if count == k:
                return root.val, count
            if root.right:
                tar_val, count = order_search(root.right, count)
                if tar_val:
                    return tar_val, count
            return None, count
        return order_search(root)[0]