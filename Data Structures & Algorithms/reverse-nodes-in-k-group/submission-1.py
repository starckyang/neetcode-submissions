class Solution:
    def reverseKGroup(self, head, k):
        # 1. 先檢查是否有 k 個 node
        count = 0
        curr = head

        while curr and count < k:
            curr = curr.next
            count += 1

        # 不足 k 個，不反轉
        if count < k:
            return head

        # 此時 curr 是下一組的開頭，也就是 next_node
        next_node = curr

        # 2. 反轉前 k 個 node
        prev = None
        curr = head

        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. head 現在是這一組的尾巴，接上後面遞迴結果
        head.next = self.reverseKGroup(next_node, k)

        # 4. prev 是這一組反轉後的新頭
        return prev