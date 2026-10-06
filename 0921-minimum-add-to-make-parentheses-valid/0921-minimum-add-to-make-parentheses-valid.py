class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additions = 0 

        for char in s:
            if char == '(':
                balance +=1

            elif balance > 0 :
                balance -= 1

            else:
                additions += 1

        return balance+additions