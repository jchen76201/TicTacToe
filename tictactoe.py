# Tic Tac Toe command line program for Recurse Center pair programming
# Author: Jason Chen
# Date created: 4/27/2025

class TicTacToe:
    def __init__(self, boardSize=3):
        self.boardSize = boardSize
        self.board = [[" " for _ in range(self.boardSize)] for _ in range(self.boardSize)]
        self.sampleBoard = [["1", "2", "3"],
                            ["4", "5", "6"],
                            ["7", "8", "9"]]
        self.player = 1
        self.movesMade = 0
        
    #----------------#
    # Main game code #
    #----------------#
    
    def make_move(self):
        if self.movesMade >= 9:
            print("It's a draw!")
            print()
            self.check_replay()
        else:
            if self.movesMade == 0:
                print("Welcome to Tic-Tac-Toe!")
                self.print_board()
            move = input("Player " + str(self.player) + ", please enter a move number from 1-9: ")
            coords = self.valid_move(move)
            while not coords:
                move = input("Please input a valid move from 1-9: ")
                coords = self.valid_move(move)
            row, col = coords
            
            symbol = "X" if self.player == 1 else "O"
            self.board[row][col] = symbol
            self.movesMade += 1
            self.print_board()
            if not self.check_win():
                self.player = 3 - self.player # Alternates between 1 and 2
                self.make_move()
            else:
                print("Player", self.player, "wins!")
                print()
                self.check_replay()
    
    #------------------#
    # Helper functions #
    #------------------#
    
    # Prints board upside down to match numpad layout
    def print_board(self):
        divider = "---+---+---"
        rowsText = [" " + self.board[i][0] + " | " + self.board[i][1] + " | " + self.board[i][2] + " " for i in range(self.boardSize)]
        sampleRowsText = [" " + self.sampleBoard[i][0] + " | " + self.sampleBoard[i][1] + " | " + self.sampleBoard[i][2] + " " for i in range(self.boardSize)]
        spacing = "     "
        print("---------------------------------")
        print()
        print(sampleRowsText[2], spacing, rowsText[2])
        print(divider, spacing, divider)
        print(sampleRowsText[1], spacing, rowsText[1])
        print(divider, spacing, divider)
        print(sampleRowsText[0], spacing, rowsText[0])
        print()
    
    def check_replay(self):
        replay = input("Play again? (y/n): ")
        validResponses = {"y", "Y", "n", "N"}
        while replay not in validResponses:
            replay = input("Sorry, I didn't understand that. Play again? (y/n): ")
        if replay == "y" or replay == "Y":
            print()
            self.reset_game()
        elif replay == "n" or replay == "N":
            print()
            print("Thanks for playing!")
            print()
        
    def reset_game(self):
        self.board = [[" " for _ in range(self.boardSize)] for _ in range(self.boardSize)]
        self.player = 1
        self.movesMade = 0
        self.make_move()

    def valid_move(self, inputText):
        if not inputText.isnumeric():
            return False
        index = int(inputText) - 1
        row = index // self.boardSize
        col = index % self.boardSize
        if index < 0 or index > 8:
            return False
        if self.board[row][col] != " ":
            return False
        return row, col
    
    #-----------------------------#
    # Code for checking for a win #
    #-----------------------------#
    
    def check_win(self):
        if self.movesMade < 5:
            return False
        return self.check_rows() or self.check_cols() or self.check_diags()
        
    def check_rows(self):
        for i in range(self.boardSize):
            row = self.board[i]
            if len(set(row)) == 1 and row[0] != " ":
                return True
        return False

    def check_cols(self):
        for i in range(self.boardSize):
            col = [row[i] for row in self.board]
            if len(set(col)) == 1 and col[0] != " ":
                return True
        return False
        
    def check_diags(self):
        diag1 = [self.board[i][i] for i in range(self.boardSize)]
        diag2 = [self.board[i][self.boardSize - i - 1] for i in range(self.boardSize)]
        if len(set(diag1)) == 1 and diag1[0] != " ":
            return True
        if len(set(diag2)) == 1 and diag2[0] != " ":
            return True
        return False
    
                
        
def main():
    game = TicTacToe()
    game.make_move()
        
if __name__ == "__main__":
    main()