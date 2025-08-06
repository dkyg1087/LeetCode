# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        from itertools import zip_longest

        def dfs(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                yield node.val
            else:
                yield from dfs(node.left)
                yield from dfs(node.right)
        

        for leaf1,leaf2 in zip_longest(dfs(root1),dfs(root2),fillvalue = None):
            if leaf1 != leaf2:
                return False
        
        return True
        

                