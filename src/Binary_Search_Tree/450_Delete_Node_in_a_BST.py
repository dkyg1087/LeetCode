# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        targ = root
        parent = None
        
        while True:
            if targ.val == key:
                break
            elif targ.val > key:
                if targ.left:
                    parent = targ
                    targ = targ.left
                else:
                    return root
            else:
                if targ.right:
                    parent = targ
                    targ = targ.right
                else:
                    return root

        if targ.right is None:
            if parent is None:
                return targ.left
            if parent.left == targ:
                parent.left = targ.left
            else:
                parent.right = targ.left
        else:
            del_parent = targ
            del_succ = targ.right
            while del_succ.left:
                del_parent = del_succ
                del_succ = del_succ.left
            
            targ.val = del_succ.val
            
            if del_parent.right == del_succ:
                del_parent.right = del_succ.right
            else:
                del_parent.left = del_succ.right
            
        return root
            
