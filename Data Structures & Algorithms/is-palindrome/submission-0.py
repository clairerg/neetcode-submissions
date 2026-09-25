class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        lst = []
        for ch in s:
            if ch.isalnum():
                lst.append(ch.lower())
        s = ''.join(lst)

        return s == s[::-1]