from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
            a/b = 4 --> a ->b =4 and b->a = 1/4
            b/c = 1
            d/e = 3.25 

            graph can be disconnected. 
        """

        graph = defaultdict(list)
        for eq, val in zip(equations, values):
            a,b = eq
            graph[a].append([b, val])
            graph[b].append([a, 1/val])
        

        def dfs(src, target, total, visited):
            if src == target:
                return total
            visited.add(src)

            for nei, weight in graph[src]:
                if nei not in visited:
                    ans = dfs(nei, target, total*weight, visited)
                    if ans != -1:
                        return ans
            return -1

        res = []
        for src,tgt in queries:
            if src not in graph or tgt not in graph:
                res.append(-1)
            elif src == tgt:
                res.append(1)
            else:
                res.append(dfs(src, tgt,1,set()))
        
        return res





