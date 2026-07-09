from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = deque()
        directions = [[0,1], [0,-1], [1,0],[-1,0]]

        # find rotten
        for r in range(ROWS):
            for c in range(COLS):        
                if grid[r][c] == 2:
                    q.append([r,c])
                
                if grid[r][c] == 1: 
                    fresh += 1
        
        visited = set()

        while q and fresh > 0:
            # level by level
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = dr+r, dc+c
                    if nr <0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc] in (0,2):
                        continue

                    q.append([nr,nc]) # next level rotten that will soread
                    grid[nr][nc] = 2
                    fresh -= 1                 
            
            time += 1
            

        return time if fresh == 0 else -1