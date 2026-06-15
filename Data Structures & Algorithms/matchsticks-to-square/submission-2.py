class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if len(matchsticks) < 4:
            return False
        
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        # each length must be equal 
        target = total // 4
        
        matchsticks.sort() # so we can stop backtracking if currLen > target
        if matchsticks[-1] > target: return False # can't split it off

        self.ans = False

        # can only use once
        used = [False] * len(matchsticks)

        def backtrack(idx, currLen, remainingSides):
            if remainingSides == 1: # b/c all other sides have been found and we know it's valid
                self.ans = True
                return True

            if currLen == target:
                return backtrack(0, 0, remainingSides - 1) # start next backtrack

            # no more
            if idx >= len(matchsticks) or currLen > target:
                return
            
            for j in range(idx, len(matchsticks)):
                if not used[j]:
                    if currLen + matchsticks[j] > target:
                        continue
                    
                    used[j] = True                        
                    if backtrack(j+1, currLen + matchsticks[j], remainingSides):
                        return True
                    used[j] = False
                
            return False
        
        return backtrack(0,0,4)
