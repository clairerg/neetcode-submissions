class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
                
            return s[left+1:right]
        
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        longest = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            if len(odd) > len(even) and len(odd) > len(longest):
                longest = odd
            elif len(even) > len(odd) and len(even) > len(longest):
                longest = even
        return longest



        