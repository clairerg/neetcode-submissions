from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lst = s.split()
        t_lst = t.split()
        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t

        