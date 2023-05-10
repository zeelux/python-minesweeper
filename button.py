import pygame

class Button:
    """A class to manage the buttons"""

    def __init__(self, ms_game, msg):
        """Initialize button attributes"""
        self.screen = ms_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self._background_color = (0, 255, 0)
        self.border_color_1 = lighten_color(self._background_color, 20)
        self.border_color_2 = lighten_color(self._background_color, -20)
        self._text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._text = msg
        self._prep_msg()

    @property
    def background_color(self):
      return self._background_color

    @background_color.setter
    def background_color(self, color):
      self._background_color = color
      self.border_width = 4
      self.border_color_1 = lighten_color(self._background_color, 20)
      self.border_color_2 = lighten_color(self._background_color, -20)
      self._prep_msg()

    @property
    def text_color(self):
      return self._text_color

    @text_color.setter
    def text_color(self, color):
      self._text_color = color
      self._prep_msg()

    @property
    def text(self):
      return self._text

    @text.setter
    def text(self, text):
      self._text = text
      self._prep_msg()

    def _prep_msg(self):
      if (not self._text):
        self.msg_image = None
        return

      self.msg_image = self.font.render(
        self._text,
        True,
        self._text_color,
        self._background_color
      )
      self.msg_image_rect = self.msg_image.get_rect()
      self.msg_image_rect.center = self.rect.center

    def draw_button(self):
      self.screen.fill(self._background_color, self.rect)

      # top
      pygame.draw.line(
        self.screen,
        self.border_color_2,
        (self.rect.left, self.rect.top),
        (self.rect.left + self.rect.width, self.rect.top),
        self.border_width
      )

      # left
      pygame.draw.line(
        self.screen,
        self.border_color_2,
        (self.rect.left, self.rect.top),
        (self.rect.left, self.rect.top + self.rect.height),
        self.border_width
      )

      # bottom
      pygame.draw.line(
        self.screen,
        self.border_color_1,
        (self.rect.left + self.rect.width, self.rect.top + self.rect.height),
        (self.rect.left, self.rect.top + self.rect.height),
        self.border_width
      )

      # right
      pygame.draw.line(
        self.screen,
        self.border_color_1,
        (self.rect.left + self.rect.width, self.rect.top + self.rect.height),
        (self.rect.left + self.rect.width, self.rect.top),
        self.border_width
      )

      if (self.msg_image):
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def on_click(self):
      if (self.command):
        self.command()


def lighten_color(color_input, amount):
  return (color_input[0] - amount, color_input[1] - amount, color_input[2] - amount)
