from collections import defaultdict, deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
            each lock combi is 1 step away from each other -> graph
            BFS approach 1 at a time, and only if not in dead end
        """

        deadends = set(deadends)
        q = deque()
        if "0000" in deadends:
            return -1

        def getNextCombos(curr):
            res = []
            # move foward
            # 0,0,0,0 -> [1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]
            for i in range(4):
                res.append(curr[:i] + str((int(curr[i])+1)%10) + curr[i+1:])

            # backward
            # 0,0,0,0 -> [9,0,0,0], [0,9,0,0], [0,0,9,0], [0,0,0,9]
            for i in range(4):
                res.append(curr[:i] + str((int(curr[i])-1)%10) + curr[i+1:])

            return res

        q.append((0,'0000')) # (moves, combo)
        while q:
            moves, combo = q.popleft()

            if combo == target:
                return moves
            
            nextCombos = getNextCombos(combo)
            for nextCombo in nextCombos:
                if nextCombo not in deadends:
                    q.append((moves+1, nextCombo))
                    deadends.add(nextCombo) # prevent loop, dont visit again

        return -1
        
        