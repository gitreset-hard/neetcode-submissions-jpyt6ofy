class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c, i, path):
            if i == len(word):
                return True
            

            for dr,dc in directions:
                nr,nc = dr+r, dc+c
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in path:
                    continue
                
                if board[nr][nc] == word[i]:
                    path.add((nr,nc))
                    if dfs(nr,nc,i+1 , path):
                        return True
                    path.remove((nr,nc))
            
            return False
        

        for r in range(ROWS):
            for c in range(COLS):
                path = set()
                if board[r][c] == word[0]:  
                    path.add((r,c))
                    if dfs(r,c,1,path):
                        return True
        
        return False

        



            
            
