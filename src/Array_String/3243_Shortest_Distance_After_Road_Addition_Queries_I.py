class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        cost = [0] * n
        adj = {}
        for i in range(n):
            cost[i] = i
        
        res = []

        for start,end in queries:
            if start in adj:
                adj[start].append(end)
            else:
                adj[start] = [end]
            
            for i in range(start,n):
                cost[i] = min(cost[i],cost[i-1]+1)
                if i in adj:
                    for c in adj[i]:
                        cost[c] = min(cost[c],cost[i]+1)
            res.append(cost[-1])
        
        return res