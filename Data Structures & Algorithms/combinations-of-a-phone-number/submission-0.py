class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []        
        num_to_char = {
            '1': [],
            '2': "abc",
            '3': "def",
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        curr = []
        def dfs(idx):
            if len(curr) == len(digits):
                res.append("".join(curr.copy()))
                return
            
            for char in num_to_char[digits[idx]]:
                curr.append(char)
                dfs(idx+1)
                curr.pop()
        
        dfs(0)
        return res