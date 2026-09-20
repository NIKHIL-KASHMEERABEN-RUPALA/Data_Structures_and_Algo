class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((26 - (ord(c) - ord('a'))) * i for i, c in enumerate(s, 1))