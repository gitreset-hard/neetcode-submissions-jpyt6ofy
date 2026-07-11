class TrieNode:
    def __init__(self, word=""):
        self.val = word
        self.child = {}
        self.ends_here = 0

class PrefixTree:

    def __init__(self):
        self.root = TrieNode('/')
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode(char)
            
            curr = curr.child[char]
        curr.ends_here += 1

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.child:
                return False
            curr = curr.child[char]
        
        return curr.ends_here > 0

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for char in prefix:
            if char not in curr.child:
                return False
            curr = curr.child[char]
        
        return True


        
        