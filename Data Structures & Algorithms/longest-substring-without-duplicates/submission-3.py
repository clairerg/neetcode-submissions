class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        left = 0
        curr = ""
        ans = 0
        for right in range(len(s)):
            ch = s[right]
            while ch in curr:
                left += 1
                curr = curr[1:]

            curr += ch
            ans = max(ans, right - left + 1)
        return ans



        