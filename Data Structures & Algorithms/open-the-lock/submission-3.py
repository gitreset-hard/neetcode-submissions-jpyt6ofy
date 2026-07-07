from collections import defaultdict, deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        count = 0

        deadends = set(deadends)
        
        if "0000" in deadends: return -1
        if target in deadends: return -1
        
        q = deque()
        q.append(["0000", 0])

        def next_combos(combo) -> List[str]:
            """ fwd and backward combos by 1
                0000 -> 0001, 0010, 0100, 1000, 0009, 0090,0900,9000
                000X 00X0 0X00 X000 + / - each indx
                split into 3 parts: to x, x, after x
            """
            res = []
            for i in range(4):
                up = combo[:i] + str((int(combo[i]) + 1) % 10)+ combo[i+1:]
                down = combo[:i] + str((int(combo[i]) - 1) % 10) + combo[i+1:]
                res.append(up)
                res.append(down)
            return res
            
            deadends.add("0000")

        while q:
            curr, cnt = q.popleft()

            if curr == target:
                return cnt

            # generate next combo
            possible_codes = next_combos(curr)
            for code in possible_codes:
                if code not in deadends:
                    q.append([code, cnt + 1])
                    deadends.add(code)



        return -1
            
            




        return count
