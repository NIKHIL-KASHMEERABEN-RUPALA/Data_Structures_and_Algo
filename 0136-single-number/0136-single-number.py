class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = {}

        n = len(nums)

        for num in nums:
            res[num] = res.get(num,0)+1

        for num,count in res.items():
            if count==1:
                return num 