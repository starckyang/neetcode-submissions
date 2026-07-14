# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (not head) or (not head.next):
            return False
        f, s = head.next, head
        while f and s:
            if f == s:
                return True
            if not f.next:
                return False
            f = f.next.next
            s = s.next    
        return False
            
