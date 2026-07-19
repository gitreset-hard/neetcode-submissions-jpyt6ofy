from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        allChars = set()
        adj = defaultdict(set)
        for word in words:
            for char in word:
                allChars.add(char)

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                if w1[j] != w2[j]:
                    #  backwards to have sorted answer without sorted
                    adj[w2[j]].add(w1[j])
                    break
            
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            

        def hasCycle(curr):
            if curr in path:
                return True
            if curr in visited: 
                return False

            path.add(curr)
            for nei in adj[curr]:
                if hasCycle(nei):
                    return True

            path.remove(curr)
            visited.add(curr)
            res.append(curr)
        
        path = set()
        visited = set()
        res = []

        for char in allChars:
            if char not in visited:
                if hasCycle(char):
                    return ""

        return "".join(res) if len(res) > 0 else ""
                