class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [cost[0], cost[1]]
        i=2
        n=len(cost)
        while i<n:
            min_cost.append((min(min_cost[i-1], min_cost[i-2])+cost[i]))
            i+=1

        return min(min_cost[n-1], min_cost[n-2])