import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [[0,1],[-1,0],[1,0],[0,-1]]
        ROWS,COLS = len(heights), len(heights[0])
        visited = set()

        min_heap = []
        min_heap.append([0, 0, 0])

        while min_heap:

            diff, r,c = heapq.heappop(min_heap)

            if (r,c) == (ROWS-1, COLS-1): return diff

            if (r,c) in visited:
                continue
            visited.add((r,c))

            for dr,dc in directions:
                nr,nc = dr+r, dc+c
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:continue

                next_step = abs(heights[nr][nc] - heights[r][c])    
                path_effort = max(next_step, diff)
                heapq.heappush(min_heap, [path_effort, nr,nc])
        
