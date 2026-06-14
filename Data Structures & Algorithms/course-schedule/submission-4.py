from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            make adjList
            find if possible to do pre before crs, if cycle then Not, else Yes
            directed graph
            
            3: [2]
            2: [1]
            1: [2] -> cycle
        """
        # make graph
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        def hasCycle(curr):
            if curr in currPath:
                return True
            if curr in visited:
                return False
            currPath.add(curr)
            for nei in adj[curr]:
                if hasCycle(nei):
                    return True
            
            # after checking the entire path
            currPath.remove(curr)
            visited.add(curr)
            return False
            

        currPath = set()
        visited = set() # global

        for idx in range(numCourses):
            if hasCycle(idx):
                return False
        
        return True
            
            
        
