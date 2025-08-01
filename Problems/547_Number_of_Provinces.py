class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self,size):
                self.parent = list(range(size))
                self.rank = [0] * size
            
            def find(self,x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self,x,y):
                x_parent = self.find(x)
                y_parent = self.find(y)

                if self.rank[x_parent] < self.rank[y_parent]:
                    self.parent[x_parent] = y_parent
                elif self.rank[x_parent] > self.rank[y_parent]:
                    self.parent[y_parent] = x_parent
                else:
                    self.parent[y_parent] = x_parent
                    self.rank[x_parent] += 1
        
        n = len(isConnected)
        uf = UnionFind(n)
        numberOfComponents = n

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1 and uf.find(i) != uf.find(j):
                    numberOfComponents -= 1
                    uf.union(i,j)
        
        return numberOfComponents