class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        
        # or we can do with this method as well (without array,Bottom-up)
        # a = 1
        # b = 1

        # for i in range(2, n + 1):
        #     a, b = b, a + b

        # return b

        
