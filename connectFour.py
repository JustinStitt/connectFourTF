from os import system, name
import numpy as np
ROWS, COLS = (6,7)

class connectFour():
    def __init__(self):
        self.board = np.array([[0] * COLS]* ROWS)
    def drop_piece(self,player_num, col):
        for x in range(ROWS - 1, -1, - 1):
            if(self.board[x][col] == 0):#free cell
                self.board[x][col] = player_num
                return True
        return False#invalid move
    def check_for_win(self,player_num):
        #check left to right
        for r in range(0, ROWS):
            count = 0
            for c in range(0, COLS):
                if(self.board[r][c] == player_num):
                    count += 1
                else:
                    count = 0
                if count >= 4:
                    print('Player({}) has won!'.format(player_num))
                    return True
        #check top to bottom
        for c in range(0, COLS):
            count = 0
            for r in range(ROWS - 1, -1, -1):
                if self.board[r][c] == player_num:
                    count += 1
                else:
                    count = 0
                if count >= 4:
                    print('Player({}) has won!'.format(player_num))
                    return True
        #check (diag) TL to BR
        for r in range(0, ROWS - 3):
            for c in range(0, COLS - 2):
                if(self.board[r][c] == player_num and
                self.board[r+1][c+1] == player_num and
                self.board[r+2][c+2] == player_num and
                self.board[r+3][c+3] == player_num):
                    return True
        #check (diag) TR to BL
        for r in range(0, ROWS - 3):
            for c in range(COLS - 1, 2, -1):
                if(self.board[r][c] == player_num and
                self.board[r+1][c-1] == player_num and
                self.board[r+2][c-2] == player_num and
                self.board[r+3][c-3] == player_num):
                    return True
        return False


    def print_board(self):#pretty print
        print("---->Board<----")
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                print(self.board[r][c], end = " ")
            print("")
        print("=================================")

#aux funcs
#end aux funs

#main test
def main():
    game = connectFour()
    #testing TL BR diag win con
    game.drop_piece(1,5)
    game.drop_piece(2,4)
    game.drop_piece(1,4)
    game.drop_piece(2,3)
    game.drop_piece(2,3)
    game.drop_piece(1,3)
    game.drop_piece(1,2)
    game.drop_piece(2,2)
    game.drop_piece(2,2)
    game.drop_piece(1,2)
    game.print_board()
    print(game.check_for_win(1))

if __name__ == '__main__':
    main()
