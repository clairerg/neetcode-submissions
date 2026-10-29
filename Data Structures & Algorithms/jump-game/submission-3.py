class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #dp[i] = if it is possible to jump to index i 
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                        dp[i] = True
        
        return dp[n-1]


        