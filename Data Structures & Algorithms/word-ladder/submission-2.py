from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if len(wordList) == 0: return 0

        """
            cat
            bat
            bag
            sag
            dag
            dot

            *at: [cat, bat]
            c*t: []
            ca*: []
            b*t: []
            ba*: [g]
            *ag: [bag, sag, dag]
        """
        patterns = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        
        # how to make a from this
        # each word in the pattern is related to each other: undirected graph
        graph = defaultdict(list)
        for pattern in patterns:
            for w1 in patterns[pattern]:
                for w2 in patterns[pattern]:
                    if w1 != w2:
                        graph[w1].append(w2)
                        graph[w2].append(w1)
        
        ## now we search to fin a connection from start -> end
        q = deque()
        q.append((beginWord, 1))
        seen = set()
        seen.add(beginWord)
        while q:
            curr_word, curr_count = q.popleft()
            # final condition
            if curr_word == endWord:
                return curr_count

            for neighbor in graph[curr_word]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append((neighbor, curr_count + 1))

        return 0
            


            



