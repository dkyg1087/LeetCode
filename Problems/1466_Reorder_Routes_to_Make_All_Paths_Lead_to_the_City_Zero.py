class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))
        visited = set()
        res = [0]

        def dfs(city,graph,visited,res):
            visited.add(city)

            for neighbor , cost in graph[city]:
                if neighbor not in visited:
                    res[0] += cost
                    dfs(neighbor,graph,visited,res)
        dfs(0,graph,visited,res)

        return res[0]
