from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
            a / b = 2 : a = 2b 
            b / c = 3 : b = 3c 

            # is the num a weight?

            a -> b = 2
            b -> a = 1/2
            b -> c = 3
            c -> b = 1/3

            x -> _ = -1

            approach:
                a / b = 2
                path from a->b costs 2*
                path from b->a costs 0.5* --> double sided
                var not in graph, -1
                var == x, -1
                a / c : is there a path from a -> c
        """

        graph = defaultdict(list)
        for idx,val in enumerate(values):
            # var1 -> var2 = val
            var1, var2 = equations[idx]
            graph[var1].append([var2, val])
            graph[var2].append([var1, 1/val])
        
        # find path and 
        # cycles? i don't thinks so?
        def dfs(src, target, ans):
            nonlocal res
            if src in curr_path:
                return False
            curr_path.add(src)
            if src == target:
                res.append(ans)
                return True
            
            for nei, weight in graph[src]:
                if dfs(nei, target, ans*weight):
                    return True
            
            curr_path.remove(src)
            # no match found 
            return False


        res = []
        for var1, var2 in queries:
            if var1 not in graph or var2 not in graph:
                res.append(-1)
                continue
            curr_path = set()
            if not dfs(var1, var2, 1):
                res.append(-1)
        return res
            









