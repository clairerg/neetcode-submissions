class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        curr = ""
        ans = 0
        for right in range(len(s)):
            ch = s[right]
            while ch in curr:
                curr = curr[1:]
                left += 1
            curr += ch
            ans = max(ans, right - left + 1)
        return ans

        