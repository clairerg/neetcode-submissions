class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        smallest = float("inf")
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < smallest:
                smallest = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        return smallest
            


        