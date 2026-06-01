"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        events = []
        for event in intervals:
            events.append((event.start, 1))
            events.append((event.end, -1))
        
        events.sort(key=lambda x: (x[0], x[1]))
        
        rooms = 0
        for start, room in events:
            rooms += room
            if rooms > 1:
                return False
        
        return True