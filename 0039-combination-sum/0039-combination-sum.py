class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        current = []

        def backTracking(start,remaining):
            if remaining == 0:
                result.append(current.copy())

            if remaining < 0 :
                return 

        
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                backTracking(i,remaining-candidates[i])
                current.pop()

        backTracking(0,target)
        return result