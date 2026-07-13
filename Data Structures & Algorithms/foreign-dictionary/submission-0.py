from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        allchars = set(char for word  in words for char in word)

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            for i in range(min_len):
                if w1[i] != w2[i]:
                    adj[w2[i]].append(w1[i])
                    break
                    # anything after can't be used to determine sort order

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""


        res = []
        visited = set()
        path = set()
        def hasCycle(node):

            if node in path:
                return True
            if node in visited:
                return False

            path.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    if hasCycle(nei):
                        return True
            
            visited.add(node)
            res.append(node)
            return False
        
        # what if there's disconnected graphs?
        # cycle?
        for char in allchars:
            if char not in visited:
                if hasCycle(char):
                    return ""

        return "".join(res) if len(res) > 0 else ""













             