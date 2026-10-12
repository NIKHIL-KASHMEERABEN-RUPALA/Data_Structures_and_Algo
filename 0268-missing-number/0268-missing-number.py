class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while nums[i]<n and nums[nums[i]]!=nums[i]:
                crt_idx = nums[i]
                nums[i] , nums[crt_idx] = nums[crt_idx] , nums[i]

        for i in range(n):
            if nums[i]!=i:
                return i

        return n
