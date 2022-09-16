class Solution:
    def isValidSudoku(self, board) -> bool:

        # check if there any same number in a row
        for row in board:
            elem = []
            for j in row:
                if j != ".":
                    if j in elem:

                        return False
                    else:
                        elem.append(j)

        # check if there any same number in a column
        for i in range(len(board)):
            elem = []
            for j in range(9):
                if board[j][i] not in elem and board[j][i] != ".":
                    elem.append(board[j][i])
                elif board[j][i] != ".":
                    return False

        # check if there any same number in a 3*3 box
        # run for 3 rows at a time
        for i in range(0, 9, 3):
            # run for 3 cols at a time
            for j in range(0, 9, 3):
                elem = []
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] not in elem and board[k][l] != ".":
                            elem.append(board[k][l])
                        elif board[k][l] != ".":
                            return False

        return True
