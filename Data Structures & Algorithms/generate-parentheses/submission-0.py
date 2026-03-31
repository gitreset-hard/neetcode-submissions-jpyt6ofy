class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        openP, closeP = n, n

        def dfs(openP, closeP, curPath):
            # leaf
            if closeP == openP == 0 :
                res.append(curPath)
                return

            #can't close -> open
            if openP  > 0:
                dfs(openP-1, closeP, curPath + "(" )

            if closeP - openP > 0:
                dfs(openP, closeP-1, curPath + ")")
            
        
        dfs(n,n,"")
        return res