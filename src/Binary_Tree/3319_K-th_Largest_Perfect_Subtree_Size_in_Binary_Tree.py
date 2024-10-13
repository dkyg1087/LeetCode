# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []

        def dfs(root):
            if root == None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left == 0 and right == 0:
                res.append(1)
                return 1
            elif left > 0 and right > 0 and left == right:
                res.append(left+right+1)
                return left + right + 1
            
            return -1
    
        dfs(root)
        
        if len(res) < k:
            return -1
        else:
            return sorted(res)[-k]


        