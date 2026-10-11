
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        d = 1

        while d * d <= n:
            if n % d == 0:
                ans += nums[d - 1] * nums[d - 1]

                other = n // d
                if other != d:
                    ans += nums[other - 1] * nums[other - 1]

            d += 1

        return ans