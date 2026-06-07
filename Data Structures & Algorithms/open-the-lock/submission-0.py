from collections import defaultdict, deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        graph of combinations 1 state away, 1 fwd & 1 backward
             0000: [0001, 0010, 0100, 1000, 0009, 0090, 0900, 9000]
             0001: [0000, 0002, 0011, 0101, 1001, 9001,0901,0091]
             ...
        
        BFS with queue and the first time it's reach is a valid ans

        building graph:
            - pre-building requires building all 10^4 combinations : not great
            - improve by building graph 1 step away and appending to queue
        """
        # build graph
        graph = defaultdict(list)
        def getNextCombinations(curr) -> list:
            # 0000: [0001, 0010, 0100, 1000, 0009, 0090, 0900, 9000]
            res = []
            for i in range(len(curr)):
                # forward   
                res.append( curr[:i] + str((int(curr[i])+1)%10) + curr[i+1:])
                # backward
                res.append( curr[:i] + str((int(curr[i])-1)%10) + curr[i+1:])
            
            return res

        deadends = set(deadends) # O(1) lookup
        if "0000" in deadends:
            return -1
        visited, q = set() , deque()
        visited.add("0000") # (combo, moves)
        q.append(("0000", 0))

        while q:
            curr, move = q.popleft()

            if curr == target:
                return move
            
            nextCombos = getNextCombinations(curr)
            for combo in nextCombos:
                if combo not in visited and combo not in deadends:
                    q.append((combo, move+1))
                    visited.add(combo)
        
        return -1
            