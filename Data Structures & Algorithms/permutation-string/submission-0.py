class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if len(s1) > len(s2):
            return False
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for i in range(s1_len):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        matches = sum( 1 for i in range(26) if s1_freq[i] == s2_freq[i])

        for right in range(s1_len, s2_len):
            if matches == 26:
                return True
            
            r_idx = ord(s2[right]) - ord('a')
            s2_freq[r_idx] += 1

            if s2_freq[r_idx] == s1_freq[r_idx]:
                matches += 1
            elif s2_freq[r_idx] - 1 == s1_freq[r_idx]:
                matches -= 1

            
            l_idx = ord(s2[right - s1_len]) - ord('a')
            s2_freq[l_idx] -= 1

            if s2_freq[l_idx] == s1_freq[l_idx]:
                matches += 1
            elif s2_freq[l_idx] + 1 == s1_freq[l_idx]:
                matches -= 1
        return matches == 26

            