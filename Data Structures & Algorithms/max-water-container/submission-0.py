class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left = 0
        right = len(heights) - 1
        while left <= right:
            h1 = heights[left]
            h2 = heights[right]
            area = (right - left) * min(h1, h2)
            if h1 < h2:
                left += 1
            else:
                right -= 1
            ans = max(ans, area)
        return ans



