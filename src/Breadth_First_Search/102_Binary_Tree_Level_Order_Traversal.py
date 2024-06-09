# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Simply BFS the tree and store the val in a temp list that will append to the final res after the full rank walk through
        
        if not root:
            return []
    
        res = []

        queue = deque([root])
        while queue:
            length = len(queue)
            temp = []            
            for i in range(length):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        
        return res


        