class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)
        ans = []
        for i in range(1, len(nums)):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            suffix_prod[j] = suffix_prod[j+1] * nums[j + 1]
        for k in range(len(nums)):
            ans.append(prefix_prod[k] * suffix_prod[k])

        return ans
        
        