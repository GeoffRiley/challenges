"""
    Proper name: 'Naughts and Crosses'
    American name: 'Tic Tac Toe'
    Reason: Who on Earth has a clue?
"""
from itertools import cycle
from typing import List, Union

# Definition of game elements
# External representation of grid is numbered 1 to 9;
# internal representation of grid is numbered 0 to 8.
# Working with a 3 x 3 grid represented as a linear array of nine cells
# initialise to `DEFAULT`
DEFAULT: str = '_'
# Visualise the board cells numbered as:
#  7  8  9
#  4  5  6
#  1  2  3
# (Just like a numeric keypad!)
VALID_POSITIONS: List[int] = list(range(1, 10))
# A winning combination exists for three symbols in a row:
WINNING_COMBINATIONS = (
    (6, 7, 8), (3, 4, 5), (0, 1, 2),
    (6, 3, 0), (7, 4, 1), (8, 5, 2),
    (0, 4, 8), (6, 4, 2),
)


class BlockedCell(Exception):
    pass


class InvalidMove(Exception):
    pass


class TicTacToe:
    _board: List[str]

    def __init__(self):
        """Constructor, allocate the blank board"""
        # Create an array of cells to hold the grid positions.
        self._board = [DEFAULT] * len(VALID_POSITIONS)
        self._turn_cycle = cycle(['O', 'X'])
        self._turn = self._next_turn()
        self._move = 0

    def _next_turn(self):
        return next(self._turn_cycle)

    def __str__(self):
        """Print the board"""
        return ' ' + '\n---+---+---\n '.join(' | '.join(c for c in self._board[s * 3:(s + 1) * 3]) for s in range(3))

    @staticmethod
    def _ndx_to_cell_(ndx: int) -> int:
        return {7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8}[ndx]

    @staticmethod
    def _cell_to_ndx_(cell: int) -> int:
        return {0: 7, 1: 8, 2: 9, 3: 4, 4: 5, 5: 6, 6: 1, 7: 2, 8: 3}[cell]

    def player_move(self, target_position: int):
        """
        Attempt to place the player move

        May raise exceptions: BlockCell, InvalidMove
        """
        if target_position in VALID_POSITIONS:
            cell = self._ndx_to_cell_(target_position)
            if self._board[cell] is DEFAULT:
                self._board[cell] = self._turn
            else:
                raise BlockedCell(f'Cannot play at {target_position}, it is already held by {self._board[cell]}')
        else:
            raise InvalidMove(f'Invalid move, {target_position} not available')

    def next_player(self) -> str:
        self._turn = self._next_turn()
        return self._turn

    def find_winner(self) -> Union[str, None]:
        """Find a winner, 'O', 'X' or None"""
        for s in ['O', 'X']:
            if any(all(self._board[c] == s for c in combo) for combo in WINNING_COMBINATIONS):
                return s
        return None

    @property
    def win(self) -> bool:
        """Test if the game is won"""
        return self.find_winner() == self._turn

    @property
    def lose(self) -> bool:
        """Test if the game is lost"""
        return self.find_winner() not in [self._turn, None]

    @property
    def draw(self) -> bool:
        """Test if the game is a draw"""
        return not (any(c == DEFAULT for c in self._board))

    @property
    def win_draw_lose(self) -> bool:
        """Test if the game is still in play"""
        return self.win or self.lose or self.draw

    @property
    def player(self) -> str:
        return self._turn


if __name__ == "__main__":
    while True:
        game = TicTacToe()
        print("Let's play Naughts and Crosses!\n")
        while not game.win_draw_lose:
            print(game)
            mv = input(f'Where would you like to play your {game.player}?')
            try:
                position = int(mv)
                game.player_move(position)
                if game.win:
                    print(game)
                    print(f'**WIN** We have a WINNER!!  Well done {game.player}.')
                    break
                if game.draw:
                    print(game)
                    print('**DRAW** That was a little pointless in the end.')
                    break
                game.next_player()
            except InvalidMove:
                print(f'Poor choice, Grasshopper, "{mv}" is not and acceptable move: use the numeric keypad layout!')
            except BlockedCell:
                print(f'Sorry that spot is already taken.')
