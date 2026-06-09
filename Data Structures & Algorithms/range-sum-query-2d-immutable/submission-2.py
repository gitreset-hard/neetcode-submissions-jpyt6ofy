class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # in each row, each cell will contain the cumulative sum so far in that row + that cell
        self.matrix = matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        #  horizontal sum
        for row in range(ROWS):
            for col in range(1,COLS):
                self.matrix[row][col] += self.matrix[row][col-1]

        # vertical sum
        for col in range(COLS):
            for row in range(1, ROWS):
                self.matrix[row][col] += self.matrix[row-1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = self.matrix[row2][col2] # bottom right

        # now subtract top of the square, left of teh square and then add back the top left b/c it got removed twice
        above = self.matrix[row1-1][col2] if row1 > 0 else 0
        left = self.matrix[row2][col1-1]  if col1 > 0 else 0
        topLeft = self.matrix[row1-1][col1-1] if (row1>0 and col1>0) else 0
        return total - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)