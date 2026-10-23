class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for i, value in enumerate(nums):
            if i != value:
                ans &= i & value
        return 0 if ans == -1 else ans