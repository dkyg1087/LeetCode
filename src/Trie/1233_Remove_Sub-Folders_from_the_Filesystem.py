class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self,char,isleaf = False):
                self.char = char
                self.isLeaf = isleaf
                self.children = {}
            
            def __repr__(self):
                temp = "isLeaf" if self.isLeaf else "NotLeaf"
                return f"TrieNode: {self.char},{temp},{self.children}"

        
        head = TrieNode("@")

        for f in folder:
            split_dir = f.split("/")
            node = head
            for i in range(1,len(split_dir)):
                if node.isLeaf:
                    break
                if split_dir[i] not in node.children:
                    temp = TrieNode(split_dir[i])
                    node.children[split_dir[i]] = temp
                    node = temp
                else:
                    node = node.children[split_dir[i]]
                
                if i == len(split_dir) - 1:
                    node.isLeaf = True
        
        ans = []

        def dfs(node,cur_dir):
            cur_dir += (node.char + "/")
            if not node.isLeaf:
                for n in node.children.values():
                    dfs(n,cur_dir)
            else:
                ans.append(cur_dir[2:-1])

            return
        dfs(head,"/")
        return ans        
            


                

                
