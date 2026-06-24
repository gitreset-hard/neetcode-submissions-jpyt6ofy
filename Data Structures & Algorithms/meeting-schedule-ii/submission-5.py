"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        events = []
        for obj in intervals:
            s,e = obj.start, obj.end
            events.append([s,1])
            events.append([e,-1])
        
        events.sort(key = lambda x: (x[0],x[1]))
        # on start  and then if a meeting is starting while other is ending, 
        # the end should come first so it doens't overcount?
        
        maxRooms = 0
        curr = 0
        for time, s in events:
            curr += s
            maxRooms = max(maxRooms, curr)
        return maxRooms