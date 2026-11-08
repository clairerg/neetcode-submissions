class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        # print(prefix)
        # print(suffix)
        ans = []
        for k in range(len(nums)):
            ans.append(prefix[k] * suffix[k])
        # print(ans)
        return ans


    