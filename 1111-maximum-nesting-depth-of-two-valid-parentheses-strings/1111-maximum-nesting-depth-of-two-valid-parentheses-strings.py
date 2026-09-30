class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        d = 0
        for c in seq:
            if c == '(':
                res.append(d & 1)
                d += 1
            else:
                d -= 1
                res.append(d & 1)
        return res