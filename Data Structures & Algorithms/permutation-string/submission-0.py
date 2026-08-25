class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        c1 = Counter(s1)

        c2 = Counter(s2[:len(s1)])

        pt1,pt2 = 0, len(s1)
        
        while pt2 < len(s2):
            if c1 == c2:
                return True
            else:
                c2[s2[pt1]] -= 1
                c2[s2[pt2]] += 1

                pt1 += 1
                pt2 += 1
        
        return c1 == c2

                