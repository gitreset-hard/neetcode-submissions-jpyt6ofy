class TrieNode:
    def __init__(self):
        self.ends_here = False
        self.child = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.ends_here = True        

    def search(self, word: str) -> bool:
    
        def dfs(i, node):
            if i == len(word):
                return node.ends_here
            
            char = word[i]
            
            if char == ".":
                for child_node in node.child.values():
                    if dfs(i+1, child_node):
                        return True
                return False
            
            if char in node.child:
                return dfs(i+1, node.child[char])
            
            return False
        
        return dfs(0, self.root)
            
        
        