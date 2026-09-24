class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i , x in enumerate(nums):
            sum = 0 
            while(x):
                sum+=x%10
                x //= 10
            if sum==i:
                return i
        return -1