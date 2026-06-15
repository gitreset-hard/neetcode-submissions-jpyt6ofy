class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = []
        curr = []
        def dfs(openB, closedB):
            #valid
            if openB == closedB == 0:
                res.append("".join(curr))
                return


            if openB > 0:
                curr.append("(")
                dfs(openB - 1, closedB)
                curr.pop()

            if closedB > 0 and closedB > openB:
                curr.append(")")
                dfs(openB, closedB-1)
                curr.pop()

        dfs(n,n)
        return res
                
