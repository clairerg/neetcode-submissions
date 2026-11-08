class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            prod *= num
        if zero_count == len(nums):
            prod = 0

        print(prod)
        ans = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
            elif zero_count > 0:
                ans.append(0)
            else:
                ans.append(prod // num)
        return ans
        