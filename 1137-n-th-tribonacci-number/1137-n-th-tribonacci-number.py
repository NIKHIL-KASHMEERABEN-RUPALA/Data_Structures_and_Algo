class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0 , 1:1 , 2:1}

        def dp(i:int)->int:
            if i in memo:
                return memo[i]

            memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
            return memo[i]

        return dp(n)