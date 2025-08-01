# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        queue = deque([root,])
        root.val = 0
        cur_lvl_sum = 0
        while len(queue) != 0:
            next_lvl_sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                node.val = cur_lvl_sum - node.val
                
                if node.left:
                    next_lvl_sum += node.left.val
                    queue.append(node.left)
                if node.right:
                    next_lvl_sum += node.right.val
                    queue.append(node.right)

                if node.left and node.right:
                    node.left.val += node.right.val
                    node.right.val = node.left.val
            
            cur_lvl_sum = next_lvl_sum
        
        return root
            

               