from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        def ds(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        pairs = [(ds(v), v, i) for i, v in enumerate(nums)]
        pairs.sort()
        visited = bytearray(n)
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = 1
                    j = pairs[j][2]
        return n - cycles