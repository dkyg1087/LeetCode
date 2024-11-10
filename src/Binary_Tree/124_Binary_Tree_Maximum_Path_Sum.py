# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        cur_max = - 1 * math.inf

        def return_max(node):
            nonlocal cur_max
            temp = [node.val]
            left = None
            right = None
            if node.left:
                left = return_max(node.left)
                cur_max = max(left,cur_max)
                temp.append(node.val+left)
            if node.right:
                right = return_max(node.right)
                cur_max = max(right,cur_max)
                temp.append(node.val+right)
            
            if node.right and node.left:
                cur_max = max(left+node.val+right,cur_max)
            maxx = max(temp)
            cur_max = max(maxx,cur_max)

            return max(temp)
        
        return_max(root)

        return cur_max
