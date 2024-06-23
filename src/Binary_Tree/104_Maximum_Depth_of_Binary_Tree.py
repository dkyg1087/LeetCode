# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse_tree_dfs(node,depth):
            if node:
                left = traverse_tree_dfs(node.left,depth+1) if node.left else depth+1
                right = traverse_tree_dfs(node.right,depth+1) if node.right else depth+1
                return max(depth+1,left,right)
            
            return depth

        return traverse_tree_dfs(root,0)
            