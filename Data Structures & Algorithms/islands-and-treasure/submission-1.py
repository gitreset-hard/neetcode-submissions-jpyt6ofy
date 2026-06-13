from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
            - start from 0 -> treasure chest (BFS)
            - start from all 0s at the same time b/c that way when a chest is reacehd, it's the fastest
        """
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]        
        seen = set()

        # find all chests to trigger BFS from
        chests = set()
        seen = set()
        q = deque() # (dist, row,col)
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    chests.add((row,col))
                    q.append((0, row,col))
        
        INF = 2**31 -1

        # start BFS
        while q:
            dist, r,c = q.popleft()
            seen.add((r,c))
            for dr,dc in directions:
                nr,nc = dr+r, dc+c
                # out of bonds, skip
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc] != INF or (nr,nc) in seen:
                    continue
                
                grid[nr][nc] = dist + 1
                q.append((dist+1, nr,nc))
        






        

        



