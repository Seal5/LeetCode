class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowV = {}
        columnV = {}
        square = {}
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == '.':
                    continue

                if row not in rowV:
                    rowV[row] = {}
                if column not in columnV:
                    columnV[column] = {}
                if (row // 3, column // 3) not in square:
                    square[(row // 3, column // 3)] = {}
                
                if board[row][column] in rowV[row]:
                    return False
                if board[row][column] in columnV[column]:
                    return False
                if board[row][column] in square[(row // 3, column // 3)]:
                    return False
                
                rowV[row][board[row][column]] = board[row][column]
                columnV[column][board[row][column]] = board[row][column]
                square[(row // 3, column // 3)][board[row][column]] = board[row][column]
        
        return True