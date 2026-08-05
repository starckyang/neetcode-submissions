class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # first solution: math
        if sum(gas)<sum(cost):
            return -1

        last=0
        lowest=1000000
        idx=0
        for i in range(len(gas)):
            last=last+gas[i]-cost[i]
            if last<lowest:
                lowest=last
                idx=i
        
        return 0 if idx==len(gas)-1 else idx+1