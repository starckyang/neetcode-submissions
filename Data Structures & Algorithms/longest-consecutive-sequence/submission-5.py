class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hm=set()
        for num in nums:
            hm.add(num)

        largest=0
        for num in nums:
            if num-1 in hm:
                continue
            else:
                cnum=num
                cur_seq=1
                while cnum+1 in hm:
                    cnum+=1
                    cur_seq+=1
                largest=max(cur_seq, largest)
        
        return largest