import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        # max_so_far, (r,c)
        minHeap = []
        minHeap.append([grid[0][0], 0,0])
        ans = 0
        visited = set()
        while minHeap:
            lvl, r,c = heapq.heappop(minHeap)

            if (r,c) == (ROWS-1, COLS-1):
                return lvl

            for dr,dc in directions:
                nr,nc = dr+r, dc+c
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in visited:
                    continue
                
                # thinking maybe diff is better than grid values??
                next_level = max(grid[nr][nc], lvl) # this is wrong i think
                heapq.heappush(minHeap, [next_level, nr,nc])
                visited.add((nr,nc))
        
        

                
                



            
            