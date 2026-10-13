class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [x*x for x in nums]
        squares.sort()
        n = len(nums)
        k = n//2 

        return (sum(squares[k:]) - sum(squares[:k]))
        