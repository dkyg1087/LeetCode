class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for course,pre in prerequisites:
            adj[pre].append(course)
        #print(adj)        
        def dfs(num,visited,stack):
            if num in stack:
                #print(f"{num} in stack:{stack}")
                return False
            if num in visited:
                #print(f"{num} in visited:{visited}")
                return True
            visited.add(num)
            stack.add(num)
            for cour in adj[num]:
                if not dfs(cour,visited,stack):
                    return False
            stack.remove(num)
            return True
        
        visited = set()
        for cour in adj.keys():
            stack = set()
            if not dfs(cour,visited,stack):
                return False

        return True
        

            

