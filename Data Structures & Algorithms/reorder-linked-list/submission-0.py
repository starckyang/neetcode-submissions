# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # detecting the start of the second half (always more than the first half exclude head)
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        s = s if not f else s.next
        sec_st = s
        
        # reverse the second part
        prev_n = None
        next_n = None
        
        while sec_st:
            next_n = sec_st.next
            sec_st.next = prev_n
            prev_n = sec_st
            if not next_n:
                break
            sec_st = next_n
        
        fh = head.next
        sh = sec_st
        while sh != None:
            fh_next = fh.next
            sh_next = sh.next
            head.next = sh
            head.next.next = fh if fh != s else None
            fh = fh_next
            sh = sh_next
            head = head.next.next
        if head:
            head.next = None 
