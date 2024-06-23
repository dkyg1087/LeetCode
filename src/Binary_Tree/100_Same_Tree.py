# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(left,right):
            if left == right == None:
                return True
            elif (left == None and right != None) or (right == None and left != None):
                return False
            if left.val != right.val:
                return False
            else:
                return traverse(left.left,right.left) and traverse(left.right,right.right)
        
        return traverse(p,q)
