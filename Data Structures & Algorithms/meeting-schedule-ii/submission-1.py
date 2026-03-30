"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        counter = {}
        for interval in intervals:
            start, end = interval.start, interval.end
            counter[start] = counter.get(start,0) + 1
            counter[end] = counter.get(end,0) - 1

        counter_list = []
        for time, count in counter.items():
            counter_list.append((time, count))
        
        counter_list.sort()
        _max = 0
        _cur = 0
        for time,count in counter_list:
            _cur += count
            _max = max(_max,_cur)
        
        return _max


