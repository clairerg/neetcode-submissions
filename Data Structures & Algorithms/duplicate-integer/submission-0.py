class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contain_d = False
        arr = [];
        for n in nums:
            if n in arr:
                contain_d = True
                break
            else:
                arr.append(n)
        return contain_d
        