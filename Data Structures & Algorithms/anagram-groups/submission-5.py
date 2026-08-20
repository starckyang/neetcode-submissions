from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm_res=defaultdict(list)
        for cstr in strs:
            hm=[0]*26
            for char in cstr:
                hm[ord(char) - 97]+=1
            hm_res[tuple(hm)].append(cstr)

        return list(hm_res.values())
