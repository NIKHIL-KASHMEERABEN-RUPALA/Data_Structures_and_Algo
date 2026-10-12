class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s = sum(ord(c) for c in s)
        sum_t = sum(ord(c1) for c1 in t)

        return chr(sum_t-sum_s)