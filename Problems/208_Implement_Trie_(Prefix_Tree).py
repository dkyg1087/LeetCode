class Trie:

    class TrieNode:
        def __init__(self,char,isLeaf = False):
            self.char = char
            self.children = {}
            self.isLeaf = isLeaf

    def __init__(self):
        self.head = self.TrieNode("%")
        
    def insert(self, word: str) -> None:
        cur = self.head
        for w in word:
            if w not in cur.children:
                temp = self.TrieNode(w)
                cur.children[w] = temp
            cur = cur.children[w]
        cur.isLeaf = True  

    def search(self, word: str) -> bool:
        cur = self.head
        for w in word:
            if w not in cur.children:
                return False
            else:
                cur = cur.children[w]

        return True if cur.isLeaf else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for w in prefix:
            if w not in cur.children:
                return False
            else:
                cur = cur.children[w]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)