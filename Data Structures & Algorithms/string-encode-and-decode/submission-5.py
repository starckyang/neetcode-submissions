class Solution:

    def encode(self, strs: List[str]) -> str:
        # length should also be an important information...
        if len(strs)==0:
            return ""
        lengths=[]
        res=""
        for cstr in strs:
            lengths.append(str(len(cstr)))
        res=",".join(lengths)+"#"+"".join(strs)
        return res

 
    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        r=0
        while s[r]!="#":
            r+=1
        nums=s[:r]
        r+=1
        nums=nums.split(",")
        res=[]
        for num in nums:
            res.append(s[r:r+int(num)])
            r+=int(num)
        return res
