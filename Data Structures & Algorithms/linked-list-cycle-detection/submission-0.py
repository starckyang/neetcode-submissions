# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_hash = {}
        while head:
            if head in node_hash:
                return True
            node_hash[head] = True
            head = head.next
        return False
            
