from board import Board

class Game:
  """A class that represents a mine sweeper game"""

  def __init__(self, size = 6) -> None:
    self.size = size
    self.board = Board(size)

  def start_new_game(self):
    print("Starting new game...")
    bombs = self.get_num("How many bombs? ")

    self.board.start_game(bombs)

    while True:
      x = self.get_num(f"Enter x (1-{self.size}): ")
      y = self.get_num(f"Enter y (1-{self.size}): ")

      if x < 1 or x > self.size or y < 1 or y > self.size:
        print("Invalid coordinates. Try again.")
        continue

      if not self.board.uncover_square(x - 1, y - 1):
        break

    play_again = input("Would you like to play again? (y/n) ").upper()
    if play_again == "Y":
      self.start_new_game()

  def get_num(self, prompt):
    while True:
      try:
        return int(input(prompt))
      except ValueError:
        print("Invalid input. Try again.")

game = Game()

game.start_new_game()
