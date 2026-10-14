class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m , n = len(num1) , len(num2)
        
        res = [0]*(m+n)

        for i in range(m-1,-1,-1):
            a = ord(num1[i])-ord('0')
            for j in range(n-1,-1,-1):
                b = ord(num2[j])-ord('0')
                
                mul = a*b
                p1 = i+j
                p2 = i+j+1

                total = mul+res[p2]
                res[p2] = total%10
                res[p1] += total//10

        start = 0
        while start < len(res) and res[start]==0:
            start+=1

        return "".join(chr(d + ord('0')) for d in res[start:])
        