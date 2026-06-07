from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        build graph with wildard to find words 1 char apart and then BFS
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

        # (word, count)
        q = deque()
        q.append((beginWord,1))
        visited = set()
        while q:
            currWord, currCount = q.popleft()
            
            if currWord == endWord:
                return currCount

            for nei in graph[currWord]:
                if nei not in visited:
                    q.append((nei, currCount + 1))
                    visited.add(currWord)
        
        return 0
                    


