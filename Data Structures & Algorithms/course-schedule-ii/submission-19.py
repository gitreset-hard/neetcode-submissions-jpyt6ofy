class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        visited = set() # cache
        path = set() # to detect cycle
        res = []
        def hasCycle(crs):
            # cycle found
            if crs in path:
                return True
            if crs in visited:
                return False

            # track curr path
            path.add(crs)
            for pre in graph[crs]:
                if hasCycle(pre):
                    return True
            
            
            visited.add(crs) # mark safe, no cycle
            res.append(crs) # the pre req is taken first
            path.remove(crs)
            return False


        for idx in range(numCourses):
            if hasCycle(idx):
                return []
    
        return res
