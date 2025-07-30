"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:


    # Do a dfs on the graph but store visited in a dict to not cycle, add the adjacent nodes after.

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def dfs(node,visited):
            for neighbor in node.neighbors:
                flag = False
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(val = neighbor.val)
                    flag = True
                
                visited[neighbor.val].neighbors.append(visited[node.val])
                if flag:
                    dfs(neighbor,visited)
            return
        
        visited = {node.val:Node(val = node.val)}
        dfs(node,visited)

        return visited[1]