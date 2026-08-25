class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        pt1 = 0
        pt2 = len(t)
        c1 = Counter(s[pt1:pt2])
        c2 = Counter(t)
        
        best_pt1,best_pt2 = None,None

        target = len(c2)
        current = sum(1 for char in c2 if c1[char] >= c2[char])

        while pt2 <= len(s):
            if current == target:
                if best_pt2 is None or best_pt2 - best_pt1 > pt2 - pt1:
                    best_pt1,best_pt2 = pt1,pt2
                
                c1[s[pt1]] -= 1

                if c1[s[pt1]] >= 0 and c1[s[pt1]] < c2[s[pt1]]:
                    current -= 1
                
                pt1 += 1

            elif pt2 == len(s):
                break
            else:
                c1[s[pt2]] += 1
                
                if c2[s[pt2]] != 0 and c1[s[pt2]] == c2[s[pt2]]:
                    current += 1
                pt2 += 1

        return s[best_pt1:best_pt2] if best_pt2 is not None else ""

