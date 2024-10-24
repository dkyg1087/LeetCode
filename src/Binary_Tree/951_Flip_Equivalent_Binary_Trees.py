# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1  or not root2 or root1.val != root2.val:
            return False
        
        if  {root1.left.val if root1.left else None,root1.right.val if root1.right else None} != \
            {root2.left.val if root2.left else None,root2.right.val if root2.right else None}:
            return False
        
        return  (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)) or \
                (self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left))

            
        