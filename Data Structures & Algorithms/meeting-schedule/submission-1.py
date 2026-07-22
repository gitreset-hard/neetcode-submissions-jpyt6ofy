"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) <= 1: return True

        events = []
        for interval in intervals:
            s,e = interval.start, interval.end
            events.append([s,1])
            events.append([e,-1])
        
        events.sort()
        curr = 0
        for time, event in events:
            curr += event
            if curr > 1:
                return False
        return True
