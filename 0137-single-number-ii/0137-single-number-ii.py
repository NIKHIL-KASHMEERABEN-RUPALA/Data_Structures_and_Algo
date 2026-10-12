class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1

        for val , count in freq.items():
            if count==1:
                return val
                