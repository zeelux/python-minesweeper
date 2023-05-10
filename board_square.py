import pygame
from button import Button

UNKNOWN = 0
BOMB = 1
SAFE = 2

class BoardSquare(Button):

  def __init__(self, ms_game, x, y):
    super().__init__(ms_game, msg=None)
    self.rect = pygame.Rect(x, y, 50, 50)
    self.background_color = (124, 124, 124)
    self._status = UNKNOWN

  @property
  def status(self):
    return self._status

  @status.setter
  def status(self, status):
    self._status = status
    self._text = "T" if status in [UNKNOWN, SAFE] else "B"
    self._prep_msg()
