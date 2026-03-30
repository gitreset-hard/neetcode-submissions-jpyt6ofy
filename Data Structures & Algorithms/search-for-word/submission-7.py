class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r,c, idx):
            if idx == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in path:
                return False
            

            if board[r][c] != word[idx]:
                return False
            
            path.add((r,c))

            directions = ((-1,0),(1,0),(0,1),(0,-1))
            for dr,dc in directions:
                if dfs(r+dr, c+dc, idx+1):
                    return True
            
            path.remove((r,c))
            return False
        

        ROWS, COLS = len(board), len(board[0])
        path = set()
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row,col,0):
                    return True

        return False