from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        t1 = [0] * (n + 2)
        t2 = [0] * (n + 2)
        last = [-1] * 100001
        ans = 0
        total_sq = 0

        for i in range(n):
            v = nums[i]
            prev = last[v]
            L = prev + 1
            R = i

            idx = R + 1
            s1 = 0
            while idx:
                s1 += t1[idx]
                idx -= idx & -idx
            idx = R + 1
            s2 = 0
            while idx:
                s2 += t2[idx]
                idx -= idx & -idx
            pR = s1 * (R + 1) - s2

            if L:
                idx = L
                s1 = 0
                while idx:
                    s1 += t1[idx]
                    idx -= idx & -idx
                idx = L
                s2 = 0
                while idx:
                    s2 += t2[idx]
                    idx -= idx & -idx
                pL = s1 * L - s2
            else:
                pL = 0

            sum_A = pR - pL
            total_sq = (total_sq + 2 * sum_A + (R - L + 1)) % MOD

            iL = L + 1
            idx = iL
            while idx <= n:
                t1[idx] += 1
                t2[idx] += L
                idx += idx & -idx

            iR = R + 2
            if iR <= n:
                idx = iR
                while idx <= n:
                    t1[idx] -= 1
                    t2[idx] -= R + 1
                    idx += idx & -idx

            ans = (ans + total_sq) % MOD
            last[v] = i

        return ans