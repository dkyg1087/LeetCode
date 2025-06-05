class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        step_before,last_step = cost[0],cost[1]

        for i in range(2,len(cost)):
            tmp_cost = min(last_step,step_before) + cost[i]
            step_before = last_step
            last_step = tmp_cost
        
        return min(last_step,step_before)
        

            
        

        
