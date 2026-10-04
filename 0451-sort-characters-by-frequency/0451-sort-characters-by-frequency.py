class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        result = []

        bucket = [[] for _ in range(len(s)+1)]

        for alphabet,count in freq.items():
            bucket[count].append(alphabet)

        for i in range(len(s),0,-1):
            if bucket[i]:
                for char in bucket[i]:
                    result.append(char*i)

        return "".join(result)
