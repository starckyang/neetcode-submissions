class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for _ in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key, val in count.items():
            freq[val].append(key)

        res=[]
        for i in range(len(nums), -1, -1):
            cur = freq[i]
            while cur:
                if len(res)>=k:
                    return res
                res.append(cur.pop())
        return res