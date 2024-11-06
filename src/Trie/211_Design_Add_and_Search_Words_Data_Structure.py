class WordDictionary:
    class TrieNode():
        def __init__(self,char):
            self.char = char
            self.isLeaf = False
            self.child = {}
            
    def __init__(self):
        self.head = self.TrieNode("%")

    def addWord(self, word: str) -> None:
        cur = self.head
        for w in word:
            if w not in cur.child:
                cur.child[w] = self.TrieNode(w)
            cur = cur.child[w]
        
        cur.isLeaf = True

    def search(self, word: str) -> bool:
        #print("=====")
        def dfs_search(node,word):
            
            cur = node
            for i in range(len(word)):
                if word[i] != "." and word[i] not in cur.child:
                    return False
                elif word[i] != '.':
                    cur = cur.child[word[i]]
                else:
                    for c in cur.child.values():
                        if dfs_search(c,word[i+1:]):
                            return True
                    return False
                
                if i == len(word) - 1 and cur.isLeaf:
                    return True
            
            return True if cur.isLeaf else False
        

        return dfs_search(self.head,word)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)