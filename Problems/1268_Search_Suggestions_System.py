class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.suggestions = []
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        def build_trie(products):
            root = TrieNode()
            for product in products:
                node = root
                for char in product:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                    if len(node.suggestions) < 3:
                        node.suggestions.append(product)
                node.isEnd = True
            
            return root
        
        products.sort()
        root = build_trie(products)
        
        ans = []
        node = root
        for char in searchWord:
            if char in node.children:
                node = node.children[char]
                ans.append(node.suggestions)
            else:
                node = TrieNode()
                ans.append([])
        return ans

            
            

        products.sort()
        ans = []
        