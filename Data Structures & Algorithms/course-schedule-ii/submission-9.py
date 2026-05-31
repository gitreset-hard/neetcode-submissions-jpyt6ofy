from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        res = []
        curr_path = set()
        res_set = set()
        # detects cycle and track courses
        def dfs(curr):
            # base case
            if curr in curr_path:
                return
            curr_path.add(curr)
            
            for neighbor in adj[curr]:
                if not dfs(neighbor):
                    return False
            
            if curr not in res_set:
                res.append(curr)
            res_set.add(curr)
            curr_path.remove(curr)
            return True                 

        for idx in range(numCourses):
            if not dfs(idx):
                return []
        
        return res
                






