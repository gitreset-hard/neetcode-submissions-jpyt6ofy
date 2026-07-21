from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = defaultdict(int)
        for i, char in enumerate(s):
            last_idx[char] = i

        res = []
        left = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end,last_idx[char])

            if i == end:
                res.append(i-left+1)
                left = i + 1

        
        return res
            
            

