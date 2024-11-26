class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        adj = {}

        if n == 1:
            return 0
        
        for a,b in edges:
            if b in adj:
                adj[b].append(a)
            else:
                adj[b] = [a]
            
            if a not in adj:
                adj[a] = []

        res = None
        for i in range(n):
            if i not in adj:
                return -1
            elif len(adj[i]) == 0:
                if res is not None:
                    return -1
                else:
                    res = i
        
        return res
            

            