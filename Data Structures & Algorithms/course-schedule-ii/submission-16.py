from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        res = []

        def dfs(curr):
            nonlocal res
            #cycle detected
            if curr in curr_path:
                return False
            
            curr_path.add(curr)
            for nei in graph[curr]:
                if not dfs(nei):
                    return False
            
            # has no neighbors, first course to be done
            curr_path.remove(curr)
            if curr not in visited:
                res.append(curr)
                visited.add(curr)
            
            return True


        # multisource dfs
        res = []
        visited = set() # global
        for idx in range(numCourses):
            curr_path = set()
            if idx not in visited:
                if not dfs(idx):
                    return []

        return res