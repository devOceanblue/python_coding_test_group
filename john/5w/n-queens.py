# https://leetcode.com/problems/n-queens/
from typing import List

class Solution:
    result = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        chessboard = [[0 for x in range(n)] for x in range(n)]

        def dfs(row: int, col: int):
            if row < 0 or col < 0: return
            if row >= n or col >= n: return
            # check chessmate
            # column check
            if chessboard[row][col] != 0: return

            # checking current position & mark checkmate position
            chessboard[row][col] = "Q"
            # increase row index
            for next_row in range(row+1, n):
                chessboard[next_row][col] += 1
                # Check diagonal
                if col+(next_row-row) < n:
                    chessboard[next_row][col+(next_row-row)] += 1
                if col-(next_row-row) >= 0:
                    chessboard[next_row][col-(next_row-row)] += 1

            for next_row in range(row+1,n):
                for next_col in range(0,n):
                    dfs(next_row, next_col)
                if "Q" not in chessboard[next_row]:
                    break

            flag = True
            for r in chessboard:
                if "Q" not in r:
                    flag = False
                    break

            if flag:
                self.result.append(["".join([att if att=="Q" else "." for att in r]) for r in chessboard])

            # revert marking
            chessboard[row][col] = 0
            for next_row in range(row+1, n):
                chessboard[next_row][col] -= 1
                if col+(next_row-row) < n: chessboard[next_row][col+(next_row-row)] -= 1
                if col-(next_row-row) >= 0: chessboard[next_row][col-(next_row-row)] -= 1

            return

        for col in range(n):
            dfs(0, col)
        return self.result

print(Solution().solveNQueens(5))