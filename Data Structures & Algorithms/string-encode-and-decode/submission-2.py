class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            length = str(len(s))
            ans += length + '#'
            ans += s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
 
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            ans.append(word)
            i = j + 1 + length

        return ans




