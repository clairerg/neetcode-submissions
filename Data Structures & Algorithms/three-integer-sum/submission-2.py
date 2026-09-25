class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            seen = set()
            target = 0 - nums[i]
            for j in range(i+1, len(nums)):
                target2 = target - nums[j]
                if target2 in seen:
                    triplet = (target2, nums[j], nums[i])
                    ans.add(triplet)
                seen.add(nums[j])
        final = []
        for triplet in ans:
            final.append(list(triplet))
        return final

        