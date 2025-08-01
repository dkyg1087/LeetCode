# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # Just store the number until you hit a leaf and return
        # made it a bit fancy with generators


        def dfs(root,number):
            
            number *= 10
            number += root.val
            
            if root.left is None and root.right is None:
                yield number
            
            else:
                if root.left:
                    yield from dfs(root.left,number)
                
                if root.right:
                    yield from dfs(root.right,number)
            
        return sum(dfs(root,0))