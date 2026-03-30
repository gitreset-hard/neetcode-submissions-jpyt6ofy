"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        counter = []
        for interval in intervals:
            counter.append((interval.start,1))
            counter.append((interval.end,-1))
        
        counter.sort()
        _max , _cur = 0, 0
        for time, count in counter:
            _cur += count
            _max = max(_max,_cur)
        
        return _max


