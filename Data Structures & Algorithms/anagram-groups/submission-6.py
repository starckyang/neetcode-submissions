from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        for cstr in strs:
            decomp="".join(sorted(cstr))
            hm[decomp].append(cstr)
        return list(hm.values())
