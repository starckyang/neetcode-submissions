class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return False
        res = set()
        for i, target in enumerate(nums):
            add_map = {}
            for t, num in enumerate(nums):
                if t > i:
                    delta = (-target)-num
                    if delta in add_map:
                        comb = ".".join(sorted([str(target), str(num), str(delta)]))
                        res.add(comb)
                    add_map[num] = True
        fin_res = []
        for com in res:
            temp = com.split(".")
            fin_res.append([int(num) for num in temp])
        return fin_res
                    
                