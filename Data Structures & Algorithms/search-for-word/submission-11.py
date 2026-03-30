class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """

        """

        def dfs(r,c, idx):
            # board bounds
            if r < 0 or c<0 or r>= ROWS or c>=COLS or (r,c) in curPath:
                return False
            
            # validate
            if board[r][c] != word[idx]:
                return False
            
            curPath.add((r,c))

            if idx == len(word) - 1:
                return True

            directions = ((-1,0),(1,0),(0,1),(0,-1))
            for dr,dc in directions:
                if dfs(r+dr, c+dc, idx + 1):
                    return True

            #backtrack
            curPath.remove((r,c))
            return False
        

        curPath = set()
        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row,col,0):
                    return True
        
        return False