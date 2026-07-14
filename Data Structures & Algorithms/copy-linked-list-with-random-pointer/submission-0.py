"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hm = {}
        ori = head
        prev = Node(0)
        while ori:
            copy = Node(ori.val)
            copy.random = ori.random
            hm[ori] = copy
            prev.next = copy
            prev = copy
            ori = ori.next
        cop_st = hm[head]
        while cop_st:
            if cop_st.random:
                cop_st.random = hm[cop_st.random]
            cop_st = cop_st.next
        return hm[head]
        