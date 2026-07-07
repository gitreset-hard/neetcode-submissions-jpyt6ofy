from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for eq, val in zip(equations, values):
            a,b = eq
            graph[a].append([b, val])
            graph[b].append([a, 1/val])
        

        def evaluate(curr, target, currVal, path):
            # dfs from start to target
            if curr == target:
                return currVal

            path.add(curr)
            for nei, factor in graph[curr]:
                if nei not in path:
                    ans = evaluate(nei, target, currVal*factor, path)
                    if ans != -1:
                        return ans
            
            return -1

        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1/1.0)
            elif start == end:
                res.append(1/1.0)
            else:
                
                res.append(evaluate(start,end,1, set()))
        
        return res
                