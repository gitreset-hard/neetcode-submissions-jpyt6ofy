from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
            [a,b] = [pre, crs]
            approach:
                make ådjList representation of directed graph
                DFS to find pre-reqs to find if u is prereq of v, 
        """
        graph = defaultdict(list)
        for pre, crs in prerequisites:
            graph[crs].append(pre)
        
        def dfs(src,target, currPath) -> bool:
            # avoid cycle
            if src in currPath:
                return False
            currPath.add(src)
            # anytime target is seen in the recursion, it's a pre-req 
            if src == target:
                return True
            
            for nei in graph[src]:
                # pre - target is found in recursion
                if dfs(nei, target, currPath):
                    return True      

            return False

        res = []
        for pre, crs in queries:
            currPath = set()
            res.append(dfs(crs,pre, currPath))

        return res





