class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq=[]
        for num in nums:
            if not subseq:
                subseq.append(num)
            else:
                if num > subseq[-1]:
                    subseq.append(num)
                else:
                    for i, sn in enumerate(subseq):
                        if num == sn:
                            break
                        if num < sn:
                            subseq[i]=num
                            break
        return len(subseq)
