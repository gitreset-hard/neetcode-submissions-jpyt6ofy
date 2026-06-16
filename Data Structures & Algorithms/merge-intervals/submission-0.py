class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals        
        
        res = []
        n = len(intervals)
        intervals.sort()
        res.append(intervals[0])

        for i in range(1,n):
            start,end = intervals[i]
            lastEnd = res[-1][1]

            if start > lastEnd:
                res.append(intervals[i])
            elif start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
        
        return res
        