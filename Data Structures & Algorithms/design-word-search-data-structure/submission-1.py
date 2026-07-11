class TrieNode:
    def __init__(self, word = ""):
        self.val = word
        self.child = {}
        self.ends_here = 0


class WordDictionary:

    def __init__(self):
        self.root = TrieNode('/')
        
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode(char)
            
            curr = curr.child[char]
        curr.ends_here += 1

    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            curr = node

            for idx in range(i, len(word)):
                if word[idx] == ".":
                    for child_node in curr.child.values():
                        if dfs(idx + 1, child_node):
                            return True
                    return False

                else:
                    if word[idx] not in curr.child:
                        return False
                    curr = curr.child[word[idx]]

            return curr.ends_here > 0

        return dfs(0,self.root)










