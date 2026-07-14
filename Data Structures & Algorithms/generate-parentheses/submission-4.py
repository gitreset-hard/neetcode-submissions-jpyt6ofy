class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(openB, closedB, path):

            if openB == closedB == 0:
                res.append("".join(path))
                return
            
            if openB > 0:
                path.append("(")
                dfs(openB - 1, closedB, path)
                path.pop()
                
            
            if closedB > 0 and closedB > openB:
                path.append(")")
                dfs(openB, closedB - 1, path)
                path.pop()

        dfs(n,n,[])
        return res

