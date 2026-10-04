class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        buckets = [[] for _ in range(len(words)+1)]

        for word,count in freq.items():
            buckets[count].append(word)

        result = []

        for i in range(len(words)-1,0,-1):
            if buckets[i]:
                buckets[i].sort()

                for word in buckets[i]:
                    result.append(word)
                    if len(result)==k:
                        return result
        return result 