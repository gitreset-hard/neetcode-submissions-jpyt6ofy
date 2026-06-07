class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        seen = set()
        wordDict = set(wordDict)
        memo = {}

        def backtrack(curr):
            if curr == "":
                return True
            
            if curr in memo:
                return  memo[curr]
            
            for word in wordDict:
                if curr.startswith(word):
                    if backtrack(curr[len(word):]):
                        memo[curr] = True
                        return True                    
            memo[curr]=False
            return False
    
        return backtrack(s)