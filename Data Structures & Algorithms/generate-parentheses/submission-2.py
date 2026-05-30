class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(openB, closeB):
            if openB == 0 and closeB == 0:
                res.append("".join(curr))
                return

            """
            can't close a bracked unless already open, 
            """
            if openB > 0:
                curr.append("(")
                dfs(openB-1, closeB)
                curr.pop()
                # openB += 1 # not sure we need this b/c the call stack holds the remaining brackets
            
            if closeB > openB:
                curr.append(")")
                dfs(openB, closeB-1)
                curr.pop()
                # closeB+= 1

        dfs(n,n)
        return res

            
