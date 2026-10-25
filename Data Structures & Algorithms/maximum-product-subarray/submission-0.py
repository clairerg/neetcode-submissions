class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #dp[i] = subarray ending in i with largest prod
        n = len(nums)
        max_dp = [float("-inf")] * n
        min_dp = [float("inf")] * n
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        for i in range(1, n):
            max_dp[i] = max(nums[i], nums[i] * max_dp[i-1], nums[i] * min_dp[i-1])
            min_dp[i] = min(nums[i], nums[i] * min_dp[i-1], nums[i] * max_dp[i-1])
        
        return max(max_dp)
