class Solution:

    def removeInvalidParentheses(self, s: str) -> list[str]:

        result = set()

        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove:
                    left_remove -= 1
                else:
                    right_remove += 1

        def dfs(index, left, right, balance, path):

            if index == len(s):
                if left == 0 and right == 0 and balance == 0:
                    result.add(''.join(path))
                return

            ch = s[index]

            if ch == '(':

                if left > 0:
                    dfs(index + 1, left - 1, right, balance, path)

                path.append(ch)
                dfs(index + 1, left, right, balance + 1, path)
                path.pop()

            elif ch == ')':

                if right > 0:
                    dfs(index + 1, left, right - 1, balance, path)

                if balance > 0:
                    path.append(ch)
                    dfs(index + 1, left, right, balance - 1, path)
                    path.pop()

            else:
                path.append(ch)
                dfs(index + 1, left, right, balance, path)
                path.pop()

        dfs(0, left_remove, right_remove, 0, [])

        return list(result)