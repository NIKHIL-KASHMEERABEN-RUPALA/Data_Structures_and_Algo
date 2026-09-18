class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        left = [n] * 26
        right = [0] * 26
        
        # Step 1: Record the leftmost and rightmost index for each character.
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            left[idx] = min(left[idx], i)
            right[idx] = i
            
        res = []
        r = -1
        
        # Step 2: Check each character at its leftmost occurrence.
        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            if i != left[char_idx]:
                continue
                
            new_r = right[char_idx]
            j = i + 1
            
            # Step 3: Expand the right boundary and validate the substring.
            while j <= new_r:
                sub_idx = ord(s[j]) - ord('a')
                if left[sub_idx] < i:
                    new_r = n
                    break
                new_r = max(new_r, right[sub_idx])
                j += 1
                
            # Step 4: If valid, add or update the result list greedily.
            if new_r < n:
                if i > r or new_r < right[ord(s[r]) - ord('a')]:
                    if i > r:
                        res.append(s[i:new_r + 1])
                    else:
                        res[-1] = s[i:new_r + 1]
                    r = new_r
                    
        return res