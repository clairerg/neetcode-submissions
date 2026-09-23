from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            extra = target - nums[i]
            if extra in dct and i != dct[extra]:
                return [dct[extra], i]
            dct[nums[i]] = i