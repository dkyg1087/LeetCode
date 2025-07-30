# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # dfs comparing left and right but mirrored

        def dfs(left,right):
            if (left is None and right is None):
                return True
            elif left and right and left.val == right.val:
                return dfs(left.right,right.left) and dfs(left.left,right.right)
            else:
                return False
        
        if root:
            return dfs(root.left,root.right)
        return False
                




