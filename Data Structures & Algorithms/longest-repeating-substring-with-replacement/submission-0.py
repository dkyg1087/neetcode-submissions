class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pt1,pt2 = 0,0
        max_freq = 0
        max_length = 0
        freq_dict = defaultdict(int)

        while pt2 < len(s):
            freq_dict[s[pt2]] += 1
            
            max_freq = max(max_freq, freq_dict[s[pt2]])

            if pt2 - pt1 + 1 - max_freq <= k:
                max_length = max(max_length, pt2 - pt1 + 1)
            
            else:
                freq_dict[s[pt1]] -= 1
                pt1 += 1

            pt2 += 1
        return max_length

