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
                if nei not in visited:
                    if not dfs(nei):
                        return False
            
            # has no neighbors, first course to be done
            if curr not in visited:
                res.append(curr)
                visited.add(curr)
            
            return True


        # multisource dfs
        res = []
        visited = set() # global
        for idx in range(numCourses):
            if idx not in visited:
                curr_path = set() # avoid cycles
                dfs(idx)

        return res if len(res) == numCourses else []