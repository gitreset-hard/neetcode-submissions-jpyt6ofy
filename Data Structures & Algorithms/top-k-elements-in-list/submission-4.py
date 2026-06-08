from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        # each idx is the freq, and value is the nums with that freq
        bucketSort = [[] for _ in range(len(nums)+1)] # to account for freq from 0 -> n
        
        for num, freq in count.items():
            bucketSort[freq].append(num)
        
        print(bucketSort, count)
        ans = []
        
        for idx in range(len(bucketSort)-1,-1,-1):
            if len(bucketSort[idx]) == 0:
                continue
            for num in bucketSort[idx]:
                ans.append(num)
                if len(ans) ==k:
                    return ans