class Solution:
    def climbStairs(self, n: int) -> int:
        # 'a' represents number of ways to climb previous stair
        # 'b' represents number of ways to climb current stair

        a = 1 
        b = 1

        for _ in range(n-1):
            a , b = b , b+a

        return b 