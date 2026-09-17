class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [n + 1] * n
        min_len = n + 1
        ans = n + 1
        
        prefix_sum = 0
        d = {0: -1}
        
        for i, x in enumerate(arr):
            prefix_sum += x
            target_sum = prefix_sum - target
            if target_sum in d:
                left = d[target_sum]
                length = i - left
                if left >= 0 and best[left] <= n:
                    ans = min(ans, length + best[left])
                if length < min_len:
                    min_len = length
            best[i] = min_len
            d[prefix_sum] = i
            
        return ans if ans <= n else -1