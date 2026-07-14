# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ht = {}
        for i, value in enumerate(preorder):
            ht[value] = i
        
        def build_tree(i=0, prev_high=-1):
            cur_high = None
            high_node = None
            while (i<len(inorder)) and (ht[inorder[i]] > prev_high):
                if high_node is None:
                    cur_high = ht[inorder[i]]
                    node = TreeNode(inorder[i])
                    high_node = node
                    i += 1
                elif ht[inorder[i]] < cur_high:
                    cur_high = ht[inorder[i]]
                    node = TreeNode(inorder[i])
                    node.left = high_node
                    high_node = node
                    i += 1
                else:
                    high_node.right, i = build_tree(i, prev_high=cur_high)
            return high_node, i

        return build_tree()[0]

            