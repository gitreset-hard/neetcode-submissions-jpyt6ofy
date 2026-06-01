"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
            0                         40
                5   10
                         15     20

            +1  +1   -1  +1     -1    -1
        """
        rooms = 0
        rooms_max = 0
        events = []
        for event in intervals:
            events.append((event.start, +1))
            events.append((event.end, -1))

        events.sort(key = lambda x: (x[0], x[1]))
        print(events)
        for time, room in events:
            rooms += room
            rooms_max = max(rooms_max, rooms)
        
        return rooms_max

            

        


