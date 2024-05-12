import random
import math


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.starting_player = random.choice(['X', 'O'])

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # check column
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def minimax(self, node, depth, alpha, beta, maximizingPlayer):  # Alpha-Beta Pruning # noqa
        if node.current_winner:
            return {'position': None,
                    'score': 1} if node.current_winner == 'X' else {'position': None, 'score': -1} if node.current_winner == 'O' else {'position': None, 'score': 0}  # X is maximizingPlayer, O is minimizingPlayer # noqa
        elif not node.empty_squares():
            return {'position': None, 'score': 0}

        if maximizingPlayer:
            maxEval = {'position': None, 'score': -math.inf}
            for move in node.available_moves():
                child = node
                child.make_move(move, 'X')
                eval = self.minimax(child, depth-1, alpha, beta, False)
                if eval['score'] > maxEval['score']:
                    maxEval['position'] = move
                    maxEval['score'] = eval['score']
                alpha = max(alpha, eval['score'])
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = {'position': None, 'score': math.inf}
            for move in node.available_moves():
                child = node
                child.make_move(move, 'O')
                eval = self.minimax(child, depth-1, alpha, beta, True)
                if eval['score'] < minEval['score']:
                    minEval['position'] = move
                    minEval['score'] = eval['score']
                beta = min(beta, eval['score'])
                if beta <= alpha:
                    break
            return minEval

    def play(self):
        if self.starting_player == 'X':
            player = 'X'
            # computer = 'O'
        else:
            player = 'O'
            # computer = 'X'

        while self.empty_squares():
            self.print_board()
            print()
            if player == 'X':
                while True:
                    try:
                        square = int(input("Make your move (1-9): ")) - 1
                        if 1 <= square+1 <= 9 and self.board[square] == ' ':
                            break
                        else:
                            print("Invalid move! Please choose an empty square between 1 and 9.") # noqa
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 9.") # noqa

                self.make_move(square, 'X')
                player = 'O'
            else:
                move = random.choice(self.available_moves())
                self.make_move(move, 'O')
                player = 'X'

            if self.current_winner:
                self.print_board()
                if self.current_winner == 'X':
                    print("Player X wins!")
                elif self.current_winner == 'O':
                    print("Player O wins!")
                return
        print("It's a tie!")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
