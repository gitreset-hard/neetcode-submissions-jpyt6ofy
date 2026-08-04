from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        res = []
        while count:

            start = min(count.keys())
            curr = []
            for i in range( groupSize):
                if (start + i) not in count:
                    return False
                
                count[start + i] -= 1
                if count[start + i] == 0:
                    del count[start + i]
            
            res.append(curr)
        
        return True