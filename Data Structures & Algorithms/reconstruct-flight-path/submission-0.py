from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        for src,dst in tickets:
            adj[src].append(dst)
        
        for src in adj:
            adj[src].sort(reverse=True)

        res = []
        visited = set()

        def dfs(node):
            
            while adj[node]:
                popped = adj[node].pop()
                dfs(popped)
            res.append(node)

        dfs("JFK")
        return res[::-1]