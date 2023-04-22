import sys
import pygame

from board import Board
from button import Button

class MineSweeperGameUI:
  """The main game GUI class"""

  def __init__(self) -> None:
    pygame.init()
    self.clock = pygame.time.Clock()

    self.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mine Sweeper")
    self.bg_color = (230, 230, 230)

    self.is_active = False
    self.play_button = Button(self, "Play")
    self.play_button.command = lambda: self.gameBoard.start_game(3)
    self.play_button.button_color = (24, 24, 24)
    self.gameBoard = Board(6)

  def run_game(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_pos = pygame.mouse.get_pos()
          if not self.is_active and self.play_button.rect.collidepoint(mouse_pos):
            self.is_active = True
            self.play_button.on_click()

      self.screen.fill(self.bg_color)

      if (self.is_active):
        self.render_board()
      else:
        self.play_button.draw_button()

      pygame.display.flip()
      self.clock.tick(60)

  def render_board(self):
    pass

if __name__ == "__main__":
  game = MineSweeperGameUI()
  game.run_game()
