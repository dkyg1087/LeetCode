# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        length = 0
        
        def dfs(node,last,node_count):
            if node is None:
                return
            nonlocal length
            length = max(length,node_count)
            if last == "L":
                dfs(node.right,"R",node_count+1)
                dfs(node.left,"L",1)
            else:
                dfs(node.left,"L",node_count+1)
                dfs(node.right,"R",1)
        
        if root is None:
            return 0
        
        dfs(root,"*",0)

        return length
            
