# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node,cur_sum):
            nonlocal count
            if node is None:
                return
            cur_sum += node.val

            if cur_sum == targetSum:
                count += 1
            
            count += d[cur_sum - targetSum]
            d[cur_sum] += 1

            dfs(node.left,cur_sum)
            dfs(node.right,cur_sum)

            d[cur_sum] -= 1
        
        count = 0
        d = defaultdict(int)

        dfs(root,0)

        return count

        