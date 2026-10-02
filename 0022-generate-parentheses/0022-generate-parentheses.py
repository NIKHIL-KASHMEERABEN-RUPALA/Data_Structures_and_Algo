class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp = [[] for _ in range(n + 1)]
        
        dp[0] = [""]
        
        for i in range(1, n + 1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i - 1 - j]:
                        dp[i].append(f"({left}){right}")
                        
        return dp[n]