from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = Counter(nums)

        for num in dct:
            if dct[num] > 1:
                return True
        return False
        