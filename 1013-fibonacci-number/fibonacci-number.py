class Solution:
    def fib(self, n: int) -> int:

        # basic way for solving using recursion(TC= O(2^n))
        # if n<=2:
        #     return 1
        # return self.fib(n - 1) + self.fib(n - 2)

        # no using Recursion + Memoization (TC = O(n))
        # memo={}
        # def solve(n):
        #     if n<=1:
        #         return n
        #     if n in memo:
        #         return memo[n]
        #     memo[n]=solve(n-1)+solve(n-2)
        #     return memo[n]

        # return solve(n)

        # Bottom - Up approach also known as Tabulation (TC=O(n))
        if n<=1:
            return n

        a=0
        b=1
        for i in range(2,n+1):
            c=a+b
            a,b=b,c
        return b




        
          