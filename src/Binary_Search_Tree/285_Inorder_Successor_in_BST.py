# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)
        
        prev = False
        for value in inorder(root):
            if prev:
                return value
            if value == p:
                prev = True
        
        return None
            
        

        