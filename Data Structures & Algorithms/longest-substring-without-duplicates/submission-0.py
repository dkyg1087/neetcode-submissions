class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pt1,pt2 = 0,0
        max_len = 0

        seen = set()

        while pt2 < len(s):
            if s[pt2] not in seen:
                seen.add(s[pt2])
                pt2 += 1
                max_len = max(max_len,pt2-pt1)
            
            else:
                while pt1 < pt2:
                    seen.remove(s[pt1])
                    if s[pt1] == s[pt2]:
                        pt1+= 1
                        break
                    else:
                        pt1 += 1    
        
        return max_len




            