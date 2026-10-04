class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n<2:
            return 0

        mn , mx = min(nums) , max(nums)
        if mn==mx:
            return 0
        
        gap = max(1,(mx-mn+n-2)//(n-1))
        size = (mx-mn)//gap+ 1


        bucket_min = [float('inf')] *size
        bucket_max = [float('-inf')] *size

        for num in nums:
            idx = (num-mn)//gap
            bucket_min[idx] = min(bucket_min[idx],num)
            bucket_max[idx] = max(bucket_max[idx],num)
        
        ans = 0
        prev = mn

        for i in range(size):
            if bucket_min[i] == float('inf'):
                continue
            
            ans = max(ans,bucket_min[i]-prev)
            prev = bucket_max[i]
        
        
        return ans