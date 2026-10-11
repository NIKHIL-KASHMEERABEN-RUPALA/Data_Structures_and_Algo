class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n 
        dp[0] = 0 

        for i in range(n):

            for j in range(i+1,min(n,i+nums[i]+1)):
                dp[j] = min(dp[j],dp[i]+1)

        return dp[-1]