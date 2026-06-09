class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # in each row, each cell will contain the cumulative sum so far in that row + that cell
        self.matrix = matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS):
            for col in range(1,COLS):
                self.matrix[row][col] += self.matrix[row][col-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # if row1<0 or row2<0 or row1>=ROWS or row2>ROWS or col1<0 or col2<0 or col2>=COLS or col1>COLS:
        #     return -1
        
        sumPerRow = 0
        # get horizontal sum per row and then add that
        for row in range(row1, row2+1):
            sumPerRow += self.matrix[row][col2] - (self.matrix[row][col1-1] if col1 > 0 else 0)
        
        return sumPerRow



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)