class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def dfs(remaining):

            if remaining == "":
                return True
            
            if remaining in memo: return memo[remaining]
            
            for word in wordDict:
                if remaining.startswith(word):
                    if dfs(remaining[len(word):]):
                        memo[remaining] = True
                        return True
            memo[remaining] = False

            return False
        
        return dfs(s)