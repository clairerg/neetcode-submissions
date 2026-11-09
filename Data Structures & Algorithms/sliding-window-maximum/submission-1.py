from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        for right in range(len(nums)):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)
            
            left = right - k + 1
            if queue and left > queue[0]:
                queue.popleft()

            if right >= k -1:
                ans.append(nums[queue[0]])
        
        return ans
        

                
        