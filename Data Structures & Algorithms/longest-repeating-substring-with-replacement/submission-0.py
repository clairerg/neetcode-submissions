from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        left = 0
        ans = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            max_freq = max(counts.values())
            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
            





        
        