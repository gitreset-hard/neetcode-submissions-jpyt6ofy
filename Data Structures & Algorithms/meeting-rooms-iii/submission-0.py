import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
            0: 20,
            1:    10 ,  
            2:      5,  9

        """
        meetings.sort(reverse=True)
        
        freeRooms = [i for i in range(n)] # minHeap
        heapq.heapify(freeRooms)
        usedRooms = []  #minHeap (endTime, room)
        roomCounts = [0] * n

        while meetings:
            start, end = meetings.pop()

            # start after it ends
            while usedRooms and start >= usedRooms[0][0]:
                _, room = heapq.heappop(usedRooms)
                heapq.heappush(freeRooms, room)

            if freeRooms: # push next meeting in to used
                room = heapq.heappop(freeRooms)
                heapq.heappush(usedRooms, (end, room))
        
            else:
                # when is the next room available?
                nextEnd , room = heapq.heappop(usedRooms)
                duration = end - start

                heapq.heappush(usedRooms, (duration + nextEnd, room))
            
            roomCounts[room] += 1
        
        return roomCounts.index(max(roomCounts))