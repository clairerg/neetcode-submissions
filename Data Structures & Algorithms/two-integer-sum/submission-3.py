class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            left = target - nums[i]
            if left in dct:
                return [dct[left], i]
            dct[nums[i]] = i
        

        