class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        water = [0] * len(height)
        left_max = [0] * len(height)
        left_max[0] = height[0]
        right_max = [0] * len(height)
        right_max[len(height)-1] = height[len(height)-1]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
        for j in range(len(height) - 2, -1, -1):
            right_max[j] = max(right_max[j+1], height[j])
        for i in range(1, len(height)-1):
            water[i] = min(left_max[i], right_max[i]) - height[i]
        
        # print(left_max)
        # print(right_max)
        # print(height)
        # print(water)
        return sum(water)



            

        