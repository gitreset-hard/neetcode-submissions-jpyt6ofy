class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def bs(row):
            l = 0
            r = len(row)
            while l <= r:
                mid = (l+r) // 2
                if row[mid] > target:
                    r = mid - 1
                elif row[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return -1 

        for row in matrix:
            if row[0] <= target <= row[-1]:
                return bs(row) > -1

        return False