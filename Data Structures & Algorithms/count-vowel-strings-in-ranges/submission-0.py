class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        goodWords = []
        for word in words:
            l = 0
            r = len(word) - 1
            if word[l] in vowels and word[r]in vowels:
                goodWords.append(1)
            else:
                goodWords.append(0)
        
        prefixSum = []
        curSum =0 
        for count in goodWords:
            curSum += count
            prefixSum.append(curSum)

        ans = []
        for l,r in queries:
            leftCount = prefixSum[l-1] if l > 0 else 0
            rightCount = prefixSum[r]
            ans.append(rightCount - leftCount)
        
        return ans

        