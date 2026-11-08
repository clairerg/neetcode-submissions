class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use a hash set?
        nums_set = set(nums)
        i = 0
        ans = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                count = 0
                curr = num
                while curr in nums_set:
                    curr += 1
                    count += 1
                ans = max(ans, count)
        return ans
                
        