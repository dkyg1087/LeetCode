class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # make this a graph problem, every relation gives an edge a cost
        # everytime you go through the cost we multiply it
        # use dfs to search for a path through start to end return the cost
        
        def find(current,target,value,visited,adjList):
            if current == target:
                return value
            else:
                visited.add(current)
                for neighbor, relation in adjList[current]:
                    if neighbor not in visited:
                        result = find(neighbor,target,value*relation,visited,adjList)
                        if result != -1.0:
                            return result
                
                return -1.0
                        
            
        adjList = {}

        for equation,value in zip(equations,values):
            a,b = equation
            if a not in adjList:
                adjList[a] = [(b,value)]
            else:
                adjList[a].append((b,value))
            
            if b not in adjList:
                adjList[b] = [(a,1/value)]
            else:
                adjList[b].append((a,1/value))
        
        res = []

        for query in queries:
            target1,target2 = query
            if target1 not in adjList or target2 not in adjList:
                res.append(-1.0)
            else:
                res.append(find(target1,target2,1.0,set(),adjList))
        
        return res

