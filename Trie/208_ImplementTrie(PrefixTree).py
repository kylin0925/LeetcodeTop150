class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False
class Trie:

    def __init__(self):
        self.wordmap = {}
        self.prefixmap = {}
        self.root = TrieNode()
        #print(self.root.child)

    def insert(self, word: str) -> None:
        next = self.root 
        for c in word:
            
            if c in next.child:
                #print(next.child.keys())
                next = next.child[c]
            else:
                #print("add",self.root, next, next.child, c)
                next.child[c] = TrieNode()
                next = next.child[c]
        next.is_end=True   
        #print(self.root.child.keys())
    def search(self, word: str) -> bool:
        nn = self.root
        for c in word:
            if c not in nn.child:
                return False
            else:
                nn = nn.child[c]
        return nn.is_end

    def startsWith(self, prefix: str) -> bool:
        nn = self.root
        for c in prefix:
            if c not in nn.child:
                return False
            else:
                nn = nn.child[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)