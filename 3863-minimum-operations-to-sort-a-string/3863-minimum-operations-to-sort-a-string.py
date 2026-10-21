class Solution:
    def minOperations(self, s: str) -> int:
        t = ''.join(sorted(s))
        if s == t:
            return 0

        n = len(s)
        if n == 2:
            return -1

        if t[0] == s[0] or t[-1] == s[-1]:
            return 1

        s1 = list(s)
        s1[:n-1] = sorted(s1[:n-1])
        s1[1:] = sorted(s1[1:])
        if ''.join(s1) == t:
            return 2

        s2 = list(s)
        s2[1:] = sorted(s2[1:])
        s2[:n-1] = sorted(s2[:n-1])
        if ''.join(s2) == t:
            return 2

        return 3