class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dp[i] = max sum subarray ending in i
        n = len(nums)
        print(n)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        print(dp)
        return max(dp)


                
