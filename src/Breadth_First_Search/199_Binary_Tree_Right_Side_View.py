# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Traverse through the tree with BFS, for every rank we store the last element e.g. the right most element


        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            length = len(queue)
            for i in range(length):
                a = queue.popleft()
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
                if i == length-1:
                    res.append(a.val)
        return res