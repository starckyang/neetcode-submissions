"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return None

        hm = {}

        def dfs(node):
            new_node = Node(node.val, node.neighbors)
            hm[node] = new_node
            for nei in node.neighbors:
                if not nei in hm:
                    dfs(nei)
            new_neighbors = []
            for nei in node.neighbors:
                new_neighbors.append(hm[nei])
            new_node.neighbors = new_neighbors
            return new_node

        return dfs(node)
    
            






