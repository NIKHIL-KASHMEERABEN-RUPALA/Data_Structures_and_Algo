
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0

        for c in s:
            if c == '(':
                if open_needed % 2:
                    insertions += 1
                    open_needed -= 1
                open_needed += 2
            else:
                open_needed -= 1
                if open_needed < 0:
                    insertions += 1
                    open_needed = 1

        return insertions + open_needed