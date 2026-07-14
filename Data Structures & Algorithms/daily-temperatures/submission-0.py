class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        large_indice = []
        rev_res = []
        if temperatures:
            large_indice.append((len(temperatures)-1, temperatures[-1]))
            rev_res = [0]
        for i in range(len(temperatures)-2, -1, -1):
            cur_temp = temperatures[i]
            find = False
            for j in range(len(large_indice)-1, -1, -1):
                if cur_temp >= large_indice[j][1]:
                    large_indice.pop()
                else:
                    rev_res.append(large_indice[-1][0]-i)
                    large_indice.append((i, cur_temp))
                    find = True
                    break

            if not find:
                rev_res.append(0)
                large_indice.append((i, cur_temp))

        res = [rev_res[len(rev_res)-i-1] for i in range(len(rev_res))]
        return res