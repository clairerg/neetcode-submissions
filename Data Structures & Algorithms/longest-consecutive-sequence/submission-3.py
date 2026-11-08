class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        longest = 1
        if len(nums) == 0:
            return 0
        prev = nums[0]
        curr = 1
        i = 0
        while i < len(nums):
            if nums[i] == prev + 1:
                curr += 1
                if i == len(nums) - 1:
                    if curr > longest:
                        longest = curr
                prev = nums[i]
            else:
                if curr > longest:
                    longest = curr
                curr = 1
                prev = nums[i]
            i+=1
        return longest


        