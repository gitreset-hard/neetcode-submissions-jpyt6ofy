import heapq
class MedianFinder:

    def __init__(self):
        self.large = [] # minHeap
        self.small = [] # maxHeap : largest number of bottom half on top

    def addNum(self, num: int) -> None:
        # add to large or num? 
        if self.small and num < -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # balance heaps
        # small: [0,-1,-2,-3,-3] -- [4,5,6] : large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)        

    def findMedian(self) -> float:
        """compare lengths
        equal
            [-1,-2] == [3,4] -> take avg of top
                [0,-1,-2] == [3,4,5] : same
        odd
        [-1,-2] = [4]    
        take top of larger one
        """
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            if len(self.small) > len(self.large):
                return -self.small[0]  
            else:
                return self.large[0]