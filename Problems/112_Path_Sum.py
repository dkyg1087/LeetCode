# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Do a simple dfs, subtract the target with out current node value
    # If it reaches 0 and is a leaf we return true

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            res = targetSum - root.val
            if res == 0 and root.left is None and root.right is None:
                return True
            else:
                return self.hasPathSum(root.left,res) or self.hasPathSum(root.right,res)
        return False
