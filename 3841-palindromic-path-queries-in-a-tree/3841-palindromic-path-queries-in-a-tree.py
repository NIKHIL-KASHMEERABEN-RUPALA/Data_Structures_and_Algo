class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        for u in reversed(order):
            p = parent[u]
            if u != 0:
                size[p] += size[u]
                if heavy[p] == -1 or size[u] > size[heavy[p]]:
                    heavy[p] = u

        head = [0] * n
        pos = [0] * n
        cur = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1
                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))
                u = heavy[u]

        size_seg = 1
        while size_seg < n:
            size_seg <<= 1

        seg = [0] * (size_seg << 1)
        chars = list(s)

        for u, c in enumerate(chars):
            seg[size_seg + pos[u]] = 1 << (ord(c) - 97)

        for i in range(size_seg - 1, 0, -1):
            seg[i] = seg[i << 1] ^ seg[i << 1 | 1]

        def update(p, value):
            p += size_seg
            seg[p] = value
            p >>= 1
            while p:
                seg[p] = seg[p << 1] ^ seg[p << 1 | 1]
                p >>= 1

        def range_xor(l, r):
            res = 0
            l += size_seg
            r += size_seg
            while l < r:
                if l & 1:
                    res ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= seg[r]
                l >>= 1
                r >>= 1
            return res

        def path_xor(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= range_xor(pos[head[u]], pos[u] + 1)
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= range_xor(pos[u], pos[v] + 1)
            return res

        answer = []

        for query in queries:
            parts = query.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                chars[u] = c
                update(pos[u], 1 << (ord(c) - 97))
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = path_xor(u, v)
                answer.append((mask & (mask - 1)) == 0)

        return answer