class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        candidates.sort()
        result = []
        path = []
        
        def backTrack(start,remaining):
            if remaining == 0:
                result.append(path.copy())

            for i in range(start,len(candidates)):
                if candidates[i] > remaining:
                    break

                if i > start and candidates[i]==candidates[i-1]:
                    continue

                path.append(candidates[i])
                backTrack(i+1,remaining-candidates[i])
                path.pop()

        backTrack(0,target)

        return result 

            
        
        