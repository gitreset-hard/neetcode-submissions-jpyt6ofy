class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1: return intervals
        res = []
        intervals.sort()
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            lastEnd = res[-1][1]
            if intervals[i][0] > lastEnd:
                res.append(intervals[i])
            
            elif intervals[i][0] <= lastEnd:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        
        return res


            
            