from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
            i see disjointed sets

             if there's a connection bw two emails that may that's one gorup.
                (may not belong to the same name) ?

        """
        graph = defaultdict(set)
        emailToName = defaultdict()
        for name, *emails in accounts:
            for email in emails:
                graph[email].update([e for e in emails if e != email])
                emailToName[email] = name

        res = []
        
        def dfs(curr):
            path.add(curr)
            visited.add(curr)
            for nei in graph[curr]:
                if nei not in path:
                    dfs(nei)


        visited = set()
        for email, name in emailToName.items():
            # all emails in path belong to the same name
            if email not in visited:
                path = set()
                dfs(email)
                res.append([name] + sorted(list(path)))
                

        return res




            



                


                