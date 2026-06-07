import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        unweighted graph
        BFS search for minimal path, use a minHeap
        """
        ROWS, COLS = len(heights),len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        minHeap = []
        minHeap.append([0,(0,0)])
        seen = set()
        pathEfforts = [[float('inf')] * COLS for _ in range(ROWS)]

        while minHeap:
            currEffort, cell = heapq.heappop(minHeap)
            r, c = cell
            
            if r == ROWS - 1 and c == COLS - 1:
                return currEffort

            if currEffort > pathEfforts[r][c]:
                continue 

            seen.add((r,c))
            for dr,dc in directions:
                nr,nc = dr+r, dc+c
                if nr < 0 or nc < 0 or nr>=ROWS or nc>=COLS or (nr,nc) in seen:
                    continue
                
                nextEffort = max(abs(heights[r][c]-heights[nr][nc]), currEffort)
                if nextEffort < pathEfforts[nr][nc]:
                    pathEfforts[nr][nc] = nextEffort
                    heapq.heappush(minHeap, [nextEffort, (nr,nc)])
            
        return pathEfforts[ROWS-1][COLS-1]



