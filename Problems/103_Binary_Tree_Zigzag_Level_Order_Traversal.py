# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # We BFS the whole tree, utilizing the nature of double ended queue we can pop/append from left and right
        # Reverse left and right for the append when we need the zig zag


        if not root:
            return []
        
        order = False
        queue = deque([root])
        res = []
        while queue:
            length = len(queue)
            order = not order
            temp = []
            print(order)
            
            for _ in range(length):
                node = None
                if order:
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)    
                temp.append(node.val)

            res.append(temp)
        return res