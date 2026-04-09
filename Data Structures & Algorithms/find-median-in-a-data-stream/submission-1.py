import heapq
class MedianFinder:
    """
        store numbers below median in a max array ->  
        store numbers above median in a min array
    """
    def __init__(self):
        # max array to expose the largest of small number
        self.small = []
        # min array to expose smallest of large nums
        self.large = []

    def addNum(self, num: int) -> None:
        # always add to small first
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        # validate heap len 
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
               

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.small) < len(self.large):
            return self.large[0]
        
        return (-self.small[0] + self.large[0])/2

        