from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            count_top = set()
            count_bottom = set()
            for col in range(9):
                curr_top = board[row][col]
                if curr_top != '.':
                    if curr_top not in count_top:
                        count_top.add(curr_top)
                    else:
                        return False
                
                curr_bottom = board[row][col]
                if curr_bottom != '.':
                    if curr_bottom not in count_bottom:
                        count_bottom.add(curr_bottom)
                    else:
                        return False
        # print(count_top)
        # print(count_bottom)
       
        for col in range(9):
            count_left = set()
            count_right = set()
            for row in range(9):
                curr_left = board[row][col]
                if curr_left != '.':
                    if curr_left not in count_left:
                        count_left.add(curr_left)
                    else:
                        return False
                curr_right = board[row][col]
                if curr_right != '.':
                    if curr_right not in count_right:
                        count_right.add(curr_right)
                    else:
                        return False
        # print(count_left)
        # print(count_right)

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                count_square = set()
                for i in range(3):
                    for j in range(3):
                        curr = board[r+i][c+j]
                        if curr != '.':
                            if curr not in count_square:
                                count_square.add(curr)
                            else:
                                return False
                print(count_square)
        
        return True

        



        