from collections import Counter
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, start, path):
            if curr == target:
                ans.append(path[:])
                return
        
            for i in range(start, len(nums)):
                total = curr + nums[i]
                if total <= target:
                    path.append(nums[i])
                    backtrack(total, i, path)
                    path.pop()       
        ans = []
        backtrack(0, 0, [])
        return ans

            
        

        
        


