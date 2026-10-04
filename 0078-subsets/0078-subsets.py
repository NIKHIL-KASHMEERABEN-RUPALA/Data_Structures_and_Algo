class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n  = len(nums)
        res = []

        for mask in range(2**n):

            subset=[]

            while mask:
                bit = mask & -mask
                subset.append(nums[bit.bit_length()-1])
                mask ^= bit
            
            res.append(subset)

        return res