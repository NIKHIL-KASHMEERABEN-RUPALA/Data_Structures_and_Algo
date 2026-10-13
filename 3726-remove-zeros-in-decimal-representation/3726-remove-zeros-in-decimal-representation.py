class Solution:
    def removeZeros(self, n: int) -> int:
        num_str = str(n)
        res = []

        for num in num_str:
            if num!='0':
                res.append(num)
        
        num = "".join(res)
        num = int(num)
        return num
