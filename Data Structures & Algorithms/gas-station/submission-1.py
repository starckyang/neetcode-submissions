class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # first solution: math
        if sum(gas)<sum(cost):
            return -1

        resid=[0]
        for i in range(len(gas)):
            resid.append(resid[i]+gas[i]-cost[i])
        low=resid[0]
        idx=0
        for i, num in enumerate(resid):
            if num<low:
                low=num
                idx=i
        return idx