class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        dp = [0] * len(cost) # 1 for idx, 1 for going above
        dp[0] = cost[0]
        dp[1] = cost[1]
        print(dp)
        for i in range(2, len(dp)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])


        return min(dp[len(cost)-1], dp[len(cost)-2])