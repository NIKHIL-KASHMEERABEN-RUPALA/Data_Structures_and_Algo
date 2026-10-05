class Solution:
    def scoreOfParentheses(self,s:str)->int:
        score = 0
        depth = 0

        for idx,char in enumerate(s):
            if char=='(':
                depth+=1

            else:
                depth-=1

                if s[idx-1]=='(':
                    score+=1<<depth

        return score