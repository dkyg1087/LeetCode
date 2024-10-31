class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key = lambda x:x[0])

        factory_position = []
        for f in factory:
            factory_position.extend([f[0]] * f[1])
        
        robot_count = len(robot)
        factory_count = len(factory_position)

        dp = [[float('inf')] * (factory_count+1) for _ in range(robot_count+1)]

        # dp[i][j] -> the cost of the robots after the ith robot are assigned to factories after the jth factory 
        # 1. we pick this factory (cost = the cost of assigning ith robot to jth factory + the cost of i+1th robot to j+1th factory)
        # 2. we skip this factory (cost = the cost of ith robot to f+1th factory)

        for j in range(factory_count+1):
            dp[robot_count][j] = 0 # the cost is 0 after all the robots are already assigned

        for i in range(robot_count -1, -1,-1):
            for j in range(factory_count -1, -1,-1):
                assign = abs(robot[i] - factory_position[j]) + dp[i+1][j+1]
                skip = dp[i][j+1]
                dp[i][j] = min(assign,skip)
        

        return dp[0][0]