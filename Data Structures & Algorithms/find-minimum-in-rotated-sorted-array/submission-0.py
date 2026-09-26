class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = float("inf")
        for n in nums:
            if n < smallest:
                smallest = n
        return smallest

        