class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        z = nums.index(0)

        inc = True
        expected = 1

        for i in range(z + 1, n):
            if nums[i] != expected:
                inc = False
                break
            expected += 1

        if inc:
            for i in range(z):
                if nums[i] != expected:
                    inc = False
                    break
                expected += 1

        if inc:
            direct = z
            reverse_rotate_reverse = n - z + 2
            return direct if direct < reverse_rotate_reverse else reverse_rotate_reverse

        dec = True
        expected = 1

        for i in range(z - 1, -1, -1):
            if nums[i] != expected:
                dec = False
                break
            expected += 1

        if dec:
            for i in range(n - 1, z, -1):
                if nums[i] != expected:
                    dec = False
                    break
                expected += 1

        if dec:
            rotate_then_reverse = z + 2
            reverse_then_rotate = n - z
            return rotate_then_reverse if rotate_then_reverse < reverse_then_rotate else reverse_then_rotate

        return -1