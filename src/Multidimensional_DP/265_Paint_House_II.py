class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        f_min = [999999,999999]
        c_min = [999999,999999]
        
        for i in range(len(costs)):
            for j in range(len(costs[0])):
                if i != 0:
                    if costs[i-1][j] == c_min[0]:
                        costs[i][j] += c_min[1]
                    else:
                        costs[i][j] += c_min[0]
                
                if costs[i][j] < f_min[0]:
                    f_min[1] = f_min[0]
                    f_min[0] = costs[i][j]
                elif costs[i][j] < f_min[1]:
                    f_min[1] = costs[i][j]
            c_min[:] = f_min[:]
            f_min[:] = [999999,999999]
        return c_min[0]

                    
                