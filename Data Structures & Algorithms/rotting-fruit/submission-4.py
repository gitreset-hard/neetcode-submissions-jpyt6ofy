from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS , COLS = len(grid), len(grid[0])
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        minutes = 0
        q = deque()
        fresh = 0

        # find fresh fruits and rotten
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col))
                if grid[row][col] == 1:
                    fresh +=1 
        
        def makeRotten(r,c) -> bool:
            nonlocal fresh

            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] in (0,2):
                return

            q.append((r,c))
            # make rotten
            grid[r][c] = 2
            fresh -= 1

        while q and fresh > 0:
            for _ in range(len(q)):
                # rotten fruit
                row, col = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr+row, dc+col
                    makeRotten(nr, nc)

            minutes += 1
        
        return minutes if fresh == 0 else -1
