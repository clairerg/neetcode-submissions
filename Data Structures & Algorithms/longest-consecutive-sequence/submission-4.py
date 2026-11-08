class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        ans = 0
        curr = []
        i = 0
        while i < len(nums):
            if len(curr) == 0:
                curr.append(nums[i])
                i += 1
            else:
                if nums[i] == curr[-1] + 1:
                    curr.append(nums[i])
                    i += 1
                else:
                    ans = max(ans, len(curr))
                    curr = []
        ans = max(ans, len(curr))
        return ans





        