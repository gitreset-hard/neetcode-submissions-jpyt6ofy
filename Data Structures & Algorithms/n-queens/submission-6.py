class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        posD = set()
        negD = set()
        
        res = []
        curr = [ ["."] * n for _ in range(n)]

        def find(row):
            if row == n:
                res.append(["".join(r) for r in curr])
                return 

            for col in range(n):
                if col in cols or (col + row) in posD or (row - col) in negD:
                    continue
                
                cols.add(col)
                posD.add(row+col)
                negD.add(row-col)
                curr[row][col] = "Q"

                find(row + 1)

                cols.remove(col)
                posD.remove(row+col)
                negD.remove(row-col)
                curr[row][col] = "."
        

        find(0)
        return res


