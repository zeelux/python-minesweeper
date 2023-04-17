from random import randint

UNKNOWN = 0
BOMB = 1
SAFE = 2

class Board:
  """A class that represents the board of the game."""

  def __init__(self, size = 6) -> None:
    self.size = size

  def start_game (self, bombs = 3):
    print("Starting game...")
    self._clear_board()
    self._place_bombs(bombs)
    self.print_state()

  def _clear_board(self):
    print("Creating board...")
    self.board = [[UNKNOWN] * self.size for i in range(self.size)]
    self.print_state()

  def _place_bombs(self, bombs):
    for i in range(0, bombs):
      x = randint(0, self.size - 1)
      y = randint(0, self.size - 1)

      while self.board[y][x] == 1:
        x = randint(0, self.size - 1)
        y = randint(0, self.size - 1)

      self.board[y][x] = 1

  def print_state(self, is_game_over = False):
    print(chr(27) + "[2J")

    print("  1 2 3 4 5 6")
    for y in range(0, self.size):
      print(y+1, end = " ")
      for x in range(0, self.size):
        self._print_square(x, y, is_game_over)
      print()
    print()

  def _print_square(self, x, y, is_game_over):
    val_at = self.board[y][x]
    if val_at == UNKNOWN:
      print("⬜", end = "")
    elif val_at == BOMB:
      print("💣" if is_game_over else "⬜", end = "")
    elif val_at == SAFE:
      adj_bombs = self.count_adjacent_bombs(x, y)

      if (adj_bombs == 0):
        print("🟩", end = "")
      else:
        print(adj_bombs, end = " ")

  def count_adjacent_bombs(self, x, y):
    count = 0

    for i in range(-1, 2):
      for j in range(-1, 2):
        if x + i >= 0 and x + i < self.size and y + j >= 0 and y + j < self.size:
          if self.board[y + j][x + i] == 1:
            count += 1

    return count

  def reveal_adjacent_squares(self, x, y):
    for i in range(-1, 2):
      for j in range(-1, 2):
        if x + i >= 0 and x + i < self.size and y + j >= 0 and y + j < self.size:
          if self.board[y + j][x + i] == UNKNOWN:
            self.board[y + j][x + i] = SAFE
            if self.count_adjacent_bombs(x + i, y + j) == 0:
              self.reveal_adjacent_squares(x + i, y + j)

  def uncover_square(self, x, y):
    if self.board[y][x] == BOMB:
      self.print_state(True)
      print("GAME OVER! You hit a bomb!")
      return False
    else:
      self.board[y][x] = SAFE
      if (self.count_adjacent_bombs(x, y) == 0):
        self.reveal_adjacent_squares(x, y)
      self.print_state()

      return not self.is_game_won()

  def is_game_won(self):
    for y in range(0, self.size):
      for x in range(0, self.size):
        if self.board[y][x] == UNKNOWN:
          return False
    return True


b = Board()
b.start_game()
