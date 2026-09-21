class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            new_dp[num_mod] = 1
            
            for i in range(k):
                if dp[i] > 0:
                    new_mod = (i * num_mod) % k
                    new_dp[new_mod] += dp[i]
                    
            for i in range(k):
                ans[i] += new_dp[i]
                
            dp = new_dp
            
        return ans