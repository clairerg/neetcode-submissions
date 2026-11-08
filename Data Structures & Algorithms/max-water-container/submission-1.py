class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            hl = heights[left]
            hr = heights[right]
            curr = (right - left) * min(hl, hr)
            if hl > hr:
                right -= 1
            else:
                left += 1

            ans = max(ans, curr)
        
        return ans
            

        