from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        left = 0
        count_s = Counter()
        smallest = float('inf')
        need = len(count_t)
        have = 0
        ans = ""
        for right in range(len(s)):
            ch = s[right]
            count_s[ch] += 1
            if count_s[ch] == count_t[ch]:
                have += 1
            while (have == need):
                if (right - left + 1) < smallest:
                    smallest = right - left + 1
                    ans = s[left:right+1]

                count_s[s[left]] -= 1
                if count_s[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        return ans


            

            

            
        