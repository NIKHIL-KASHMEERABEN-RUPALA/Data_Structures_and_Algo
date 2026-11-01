
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        return sum(num - minimum for num in nums)
