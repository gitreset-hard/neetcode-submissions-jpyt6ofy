class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        prefixSum = [0] * (len(words) +1)
        for i in range(len(words)):
            isValid = 1 if words[i][0] in vowels and words[i][-1] in vowels else 0
            prefixSum[i+1] = prefixSum[i] + isValid

        ans = []
        for l,r in queries:
            leftCount = prefixSum[l]
            rightCount = prefixSum[r+1]
            ans.append(rightCount - leftCount)
        
        return ans

        