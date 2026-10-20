class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        arr = sorted(nums)

        def is_rotation(a, b):
            m = len(a)
            pi = [0] * m
            j = 0

            for i in range(1, m):
                while j and a[i] != a[j]:
                    j = pi[j - 1]
                if a[i] == a[j]:
                    j += 1
                pi[i] = j

            j = 0
            for i in range(2 * m - 1):
                x = b[i % m]

                while j and x != a[j]:
                    j = pi[j - 1]
                if x == a[j]:
                    j += 1
                if j == m:
                    return True

            return False

        ans = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            for start in range(0, n, k):
                if not is_rotation(
                    nums[start:start + k],
                    arr[start:start + k]
                ):
                    break
            else:
                ans += k

        return ans
