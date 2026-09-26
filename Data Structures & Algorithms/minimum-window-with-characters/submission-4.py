from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        count_t = Counter(t)
        window_s = Counter()
        count_s = Counter(s)
        formed = 0
        ans = s
        # if len(t) > len(s):
        #     return ''
        for c in count_t:
            if count_s[c] < count_t[c]:
                return ''
        for right in range(len(s)):
            window_s[s[right]] += 1
            if s[right] in count_t and window_s[s[right]] == count_t[s[right]]:
                formed += 1
            while formed == len(count_t):
                if right - left + 1 < len(ans):
                    ans = s[left:right+1]
                window_s[s[left]] -= 1
                if s[left] in count_t and window_s[s[left]] < count_t[s[left]]:
                    formed -= 1
                left += 1
        return ans

            


        