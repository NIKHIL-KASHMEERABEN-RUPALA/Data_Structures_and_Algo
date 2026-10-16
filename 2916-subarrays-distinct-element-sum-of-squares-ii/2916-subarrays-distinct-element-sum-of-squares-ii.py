from typing import List

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.sum_x = [0] * (4 * n)
        self.sum_x2 = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _apply(self, node: int, l: int, r: int, v: int) -> None:
        length = r - l + 1
        self.sum_x2[node] += 2 * v * self.sum_x[node] + v * v * length
        self.sum_x[node] += v * length
        self.lazy[node] += v

    def _push_down(self, node: int, l: int, r: int) -> None:
        if self.lazy[node]:
            mid = (l + r) // 2
            v = self.lazy[node]
            self._apply(2 * node, l, mid, v)
            self._apply(2 * node + 1, mid + 1, r, v)
            self.lazy[node] = 0

    def _push_up(self, node: int) -> None:
        self.sum_x[node] = self.sum_x[2 * node] + self.sum_x[2 * node + 1]
        self.sum_x2[node] = self.sum_x2[2 * node] + self.sum_x2[2 * node + 1]

    def update(self, node: int, l: int, r: int, ql: int, qr: int, v: int) -> None:
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self._apply(node, l, r, v)
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        self.update(2 * node, l, mid, ql, qr, v)
        self.update(2 * node + 1, mid + 1, r, ql, qr, v)
        self._push_up(node)

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        st = SegmentTree(n)
        last_pos = {}
        ans = 0
        MOD = 1_000_000_007
        for i, val in enumerate(nums):
            prev = last_pos.get(val, -1)
            st.update(1, 0, n - 1, prev + 1, i, 1)
            ans = (ans + st.sum_x2[1]) % MOD
            last_pos[val] = i
        return ans