class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = dict(knowledge)
        res = []
        i, n = 0, len(s)
        
        while i < n:
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]
                res.append(mapping.get(key, "?"))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
                
        return "".join(res)