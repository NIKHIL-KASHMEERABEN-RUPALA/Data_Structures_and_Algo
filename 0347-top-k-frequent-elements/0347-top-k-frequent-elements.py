class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        for num , count in freq.items():
            bucket[count].append(num)

        for i in range(len(nums),0,-1):
            if bucket[i]:
                result.extend(bucket[i])

                if len(result)>=k:
                    return result[:k]

        return result