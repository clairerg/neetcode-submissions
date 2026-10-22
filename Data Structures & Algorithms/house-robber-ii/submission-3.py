class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_house(lst):
            dp = [0] * len(lst)
            dp[0] = lst[0]
            for i in range(1, len(lst)):
                dp[i] = max(dp[i-1], lst[i] + dp[i-2])
            return dp[len(lst)-1]
        
        if len(nums) == 1:
            return nums[0]
        return max(rob_house(nums[1:]), rob_house(nums[:-1]))