class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] = max subseq ending at i 
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            max_length = 0
            for j in range(i):
                if nums[j] < nums[i] and dp[j] > max_length:
                    max_length = dp[j]
            dp[i] = max_length + 1
            
        return max(dp)
            
        