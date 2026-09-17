class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod =10**9+7

        dp=[[[0,0]for _ in range(k+1)]for _ in range(n)]
        dp[0][0][0]=1

        for i in range (1,n):
            for j in range(k+1):
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1])%mod
                dp[i][j][1] = dp[i-1][j][1]
                if j>0:
                    dp[i][j][1]=(dp[i][j][1]+ dp[i-1][j-1][0] + dp[i-1] [j-1][1])%mod
        return (dp[n-1][k][0] + dp[n-1][k][1])%mod           
