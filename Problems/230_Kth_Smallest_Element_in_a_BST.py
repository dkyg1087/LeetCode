# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Inoder traverse the tree and stop at the kth node

        def inorder_traverse(root):
            if root is not None:
                yield from inorder_traverse(root.left)
                yield root.val
                yield from inorder_traverse(root.right)

        for index,value in zip(range(1,k+1),inorder_traverse(root)):
            if index == k:
                return value
