class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        n = len(nums)
        max_len = -1
        cur_sum = 0
        left = 0
        
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return n - max_len if max_len != -1 else -1