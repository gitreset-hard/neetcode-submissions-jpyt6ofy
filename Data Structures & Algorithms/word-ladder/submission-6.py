from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        1. each word in the values() is 1 letter apart from each other. 
        *at: [bat, cat]
        c*t: [cat]
        ca*: [cat]
        b*t: [bat]
        ba*: [bag, bat]
        *ag: [bag, sag, dag]
        s*g: [sag]
        sa*: [sag]
        d*g: [dag, dog]
        da*: [dag]
        *ot: [dot]
        d*t: [dot]
        do*: [dog, dot]

        2. build a graph of each word 1 unit away? Undireected Graph
        3. then see if there's a path from start -> end
        """

        wildcardGraph = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                wildcardGraph[key].append(word)
        
        graph = defaultdict(list)
        for words in wildcardGraph.values():
            # bat cat dat hat
            for word in words:
                graph[word].extend([w for w in words if w!= word])


        # traverse graph to find conneciton, starting at beginWord. There must be a connection from begin <-> end

        currPath = set() # avoid cycles
        ans = float('inf')
        def dfs(curr, depth):
            nonlocal ans
            if depth > ans:
                return
            # why would I return False? don't need to?
            if curr in currPath:
                return False

            if curr == endWord:
                ans = min(ans, depth)
                return 

            currPath.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in currPath:
                    dfs(neighbor, depth + 1)
                        
            currPath.remove(curr)
            return
        dfs(beginWord, 1)

        return 0 if ans == float('inf') else ans

""" {'bat': ['cat', 'bag'], 
    'cat': ['bat'], 
    'bag': ['bat', 'sag', 'dag'], 
    'sag': ['bag', 'dag'], '
    dag': ['bag', 'sag'], 
    'dot': []
     })"""

