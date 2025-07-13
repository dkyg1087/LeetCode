# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        level = []

        def dfs(node,level,depth):
            if len(level) <= depth:
                level.append(0)

            level[depth] += node.val

            if node.left:
                dfs(node.left,level,depth+1)
            if node.right:
                dfs(node.right,level,depth+1)
            


        dfs(root,level,0)
        return max(enumerate(level),key=lambda p:p[1])[0] + 1