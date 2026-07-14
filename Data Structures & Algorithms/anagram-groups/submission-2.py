class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnts = [["0"] * 26 for _ in range(len(strs))]
        for i, s_str in enumerate(strs):
            for char in s_str:
                cnts[i][ord(char)-ord("a")] = str(int(cnts[i][ord(char)-ord("a")]) + 1)
         
        groups = {}
        for i, cnt in enumerate(cnts):
            cnt_str = ".".join(cnt)
            if cnt_str in groups:
                groups[cnt_str].append(strs[i])
            else:
                groups[cnt_str] = [strs[i]]

        return list(groups.values())