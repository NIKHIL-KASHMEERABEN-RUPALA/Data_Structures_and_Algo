from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        nums = [x % k for x in nums]
        
        tree_prod = [1] * (4 * n)
        tree_remain = [[0] * k for _ in range(4 * n)]
        
        def merge(p1, r1, p2, r2):
            p = (p1 * p2) % k
            r = list(r1)
            for i in range(k):
                r[(i * p1) % k] += r2[i]
            return p, r

        def build(node, start, end):
            if start == end:
                val = nums[start]
                tree_prod[node] = val
                tree_remain[node][val] = 1
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            p1, r1 = tree_prod[2 * node], tree_remain[2 * node]
            p2, r2 = tree_prod[2 * node + 1], tree_remain[2 * node + 1]
            tree_prod[node], tree_remain[node] = merge(p1, r1, p2, r2)

        build(1, 0, n - 1)

        def update(node, start, end, idx, val):
            if start == end:
                tree_prod[node] = val
                for i in range(k):
                    tree_remain[node][i] = 0
                tree_remain[node][val] = 1
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            p1, r1 = tree_prod[2 * node], tree_remain[2 * node]
            p2, r2 = tree_prod[2 * node + 1], tree_remain[2 * node + 1]
            tree_prod[node], tree_remain[node] = merge(p1, r1, p2, r2)

        def query(node, start, end, l, r):
            if l <= start and end <= r:
                return tree_prod[node], tree_remain[node]
            mid = (start + end) // 2
            if r <= mid:
                return query(2 * node, start, mid, l, r)
            elif l > mid:
                return query(2 * node + 1, mid + 1, end, l, r)
            else:
                p1, r1 = query(2 * node, start, mid, l, r)
                p2, r2 = query(2 * node + 1, mid + 1, end, l, r)
                return merge(p1, r1, p2, r2)

        ans = []
        for idx, val, start, xi in queries:
            val %= k
            update(1, 0, n - 1, idx, val)
            _, rems = query(1, 0, n - 1, start, n - 1)
            ans.append(rems[xi])
            
        return ans