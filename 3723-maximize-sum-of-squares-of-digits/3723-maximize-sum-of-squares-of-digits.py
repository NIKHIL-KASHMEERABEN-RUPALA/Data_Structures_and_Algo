class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Feasibility check: each digit can contribute at most 9
        if sum > 9 * num:
            return ""
        
        # Number of complete 9s and the remaining digit sum
        q, r = divmod(sum, 9)
        
        # Build the result: all 9s first (largest numerical value),
        # then the remainder digit (if any), then fill with zeros.
        ans = "9" * q
        if r > 0:
            ans += str(r)
        ans += "0" * (num - len(ans))
        
        return ans