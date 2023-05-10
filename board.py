from random import randint
import numpy as np

from board_square import BoardSquare

UNKNOWN = 0
BOMB = 1
SAFE = 2

class Board:
  """A class that represents the board of the game."""

  def __init__(self, game, size = 6) -> None:
    self.size = size
    self.ms_game = game

  def start_game (self, bombs = 3):
    print("Starting game...")
    self._clear_board()
    self._place_bombs(bombs)
    self.print_state()

  def handle_click(self, mouse_pos):
    for y in range(0, self.size):
      for x in range(0, self.size):
        if self.board[y][x].rect.collidepoint(mouse_pos):
          return self.uncover_square(x, y)

  def _clear_board(self):
    print("Creating board...")

    #self.board = [[UNKNOWN] * self.size for i in range(self.size)]

    self.board = np.array([BoardSquare(
      self.ms_game,
      (54 * int(i % self.size)) + 2,
      (54 * int(i / self.size)) + 2
    ) for i in range(self.size * self.size)]
    ).reshape(self.size, self.size)

    self.print_state()

  def _place_bombs(self, bombs):
    for i in range(0, bombs):
      x = randint(0, self.size - 1)
      y = randint(0, self.size - 1)

      while self.board[y][x].status == BOMB:
        x = randint(0, self.size - 1)
        y = randint(0, self.size - 1)

      self.board[y][x].status = BOMB

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
    square = self.board[y][x]
    square.draw_button()

    if square.status == UNKNOWN:
      print("⬜", end = "")
    elif square.status == BOMB:
      print("💣" if is_game_over else "⬜", end = "")
    elif square.status == SAFE:
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
          if self.board[y + j][x + i].status == BOMB:
            count += 1

    return count

  def reveal_adjacent_squares(self, x, y):
    for i in range(-1, 2):
      for j in range(-1, 2):
        if x + i >= 0 and x + i < self.size and y + j >= 0 and y + j < self.size:
          if self.board[y + j][x + i].status == UNKNOWN:
            self.board[y + j][x + i].status = SAFE
            if self.count_adjacent_bombs(x + i, y + j) == 0:
              self.reveal_adjacent_squares(x + i, y + j)

  def uncover_square(self, x, y):
    if self.board[y][x].status == BOMB:
      self.print_state(True)
      print("GAME OVER! You hit a bomb!")
      return False

    self.board[y][x].status = SAFE
    if (self.count_adjacent_bombs(x, y) == 0):
      self.reveal_adjacent_squares(x, y)
    self.print_state()

    is_won = self.is_game_won()

    if (is_won):
      print("Congratulations! You won!")

    return not is_won

  def is_game_won(self):
    for y in range(0, self.size):
      for x in range(0, self.size):
        if self.board[y][x].status == UNKNOWN:
          return False
    return True
