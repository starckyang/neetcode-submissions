class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = [0] * 2001
        for num in nums:
            cnts[num+1000] += 1
        sorted_cnts = sorted(cnts, reverse=True)
        threshold = sorted_cnts[k-1]
        ans = []
        for i, cnt in enumerate(cnts):
            if cnt >= threshold:
                ans.append(i-1000)
        return ans