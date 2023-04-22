import pygame.font


class Button:
    """A class to manage the buttons"""

    def __init__(self, ms_game, msg):
        """Initialize button attributes"""
        self.screen = ms_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
      self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
      self.msg_image_rect = self.msg_image.get_rect()
      self.msg_image_rect.center = self.rect.center

    def draw_button(self):
      self.screen.fill(self.button_color, self.rect)
      self.screen.blit(self.msg_image, self.msg_image_rect)


    def on_click(self):
      if (self.command):
        self.command()
