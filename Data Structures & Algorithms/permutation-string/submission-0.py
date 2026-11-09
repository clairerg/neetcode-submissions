from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        k = len(s1)
        left = 0
        c2 = Counter()
        for right in range(len(s2)):
            c2[s2[right]] += 1
            while right - left + 1 > k:
                c2[s2[left]] -= 1
                left += 1

            if right - left + 1 == k:
                if c2 == c1:
                    return True
           
        return False
        
        