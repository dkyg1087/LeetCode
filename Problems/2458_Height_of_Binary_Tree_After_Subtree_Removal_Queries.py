# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        # https://www.youtube.com/watch?v=oZsWlELiQmQ
        
        level_height_node_dict = {}
        # node -> [level,height]
        level_based_height_dict = {}
        # level -> [height1,height2]
        def find_level_height(node,level):
            if not node:
                return -1
            
            val = node.val
            lvl = level
            height = 1 + max(find_level_height(node.left,level+1),find_level_height(node.right,level + 1))
            level_height_node_dict[val] = [lvl,height]
            if lvl not in level_based_height_dict:
                level_based_height_dict[lvl] = [height,-1]
            else:
                first,secc = level_based_height_dict[lvl]
                if first < height:
                    level_based_height_dict[lvl][1] = first
                    level_based_height_dict[lvl][0] = height
                elif secc < height:
                    level_based_height_dict[lvl][1] = height
            
            return height
                    
                 
        
        find_level_height(root,0)
        
        ans = []
        for query in queries:
            lvl,height = level_height_node_dict[query]
            if len(level_based_height_dict[lvl]) == 1:
                ans.append(level_based_height_dict[lvl-1][0] + lvl - 1)
            else:
                first,secc = level_based_height_dict[lvl]
                if height == first:
                    ans.append(lvl+secc)
                elif height == secc:
                    ans.append(lvl+first)
                else:
                    ans.append(lvl+first)
        
        return ans
                


            