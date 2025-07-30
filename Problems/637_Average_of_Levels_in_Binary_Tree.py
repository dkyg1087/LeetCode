# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        # Iterate the tree using BFS with a queue.
        # For every level we just add up all the node with same level.
        
        queue = deque([root])
        res = []

        while queue:
            amount = len(queue)
            total = 0
            for i in range(amount):
                current = queue.popleft()
                total += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            res.append(total/amount)
        
        return res
                
            

        