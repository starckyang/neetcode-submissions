# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_node = ListNode()
        start = None
        adv = 0
        while l1 and l2:
            t_sum = l1.val + l2.val + adv
            adv = 0
            if t_sum >= 10:
                t_sum = t_sum % 10
                adv = 1
            sum_node.next = ListNode(t_sum)
            sum_node = sum_node.next
            if not start:
                start = sum_node
            l1, l2 = l1.next, l2.next
        remain = l1 if l1 else l2
        while remain:
            t_sum = remain.val + adv
            adv = 0
            if t_sum >= 10:
                t_sum = t_sum % 10
                adv = 1
            sum_node.next = ListNode(t_sum)
            sum_node = sum_node.next
            remain = remain.next
        if adv == 1:
            sum_node.next = ListNode(1)
        return start


            