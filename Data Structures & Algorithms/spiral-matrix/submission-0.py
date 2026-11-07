class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while (left <= right and top <= bottom):
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            # print(ans)
            
            top += 1
            if top > bottom:
                break

            for row in range(top, bottom+1):
                ans.append(matrix[row][right])
            # print(ans)
            
            right -= 1

            if left > right:
                break

            for col in range(right, left - 1, -1):
                ans.append(matrix[bottom][col])
            # print(ans)

            
            bottom -= 1
            if top > bottom:
                break
            for row in range(bottom, top-1, -1):
                ans.append(matrix[row][left])
            # print(ans)
            
            left += 1
        
        return(ans)