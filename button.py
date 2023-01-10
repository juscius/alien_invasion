import pygame.font

class Button:

	instancelist = []

	def __init__(self, ai_game, msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (0, 0, 255)
		self.button_boarder_color = (0, 0, 255)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		#Build the button's rect object and center it.
		self.rect = pygame.Rect(0,0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		#The button message needs to be prepped only once.
		self._prep_msg(msg)

		Button.instancelist.append(self)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def _update_msg_position(self):
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

	def draw_button_boarders(self):
		self.button_boarder_xpos = self.rect.x
		self.button_boarder_ypos = self.rect.y
		self.button_boarder_width, self.button_boarder_height = self.rect.size
		pygame.draw.rect(self.screen, self.button_boarder_color, (self.button_boarder_xpos, self.button_boarder_ypos,
		self.button_boarder_width, self.button_boarder_height), 5)

	def reset_button_boarders_color(self):

		for instance in Button.instancelist:
			instance.button_boarder_color = self.button_color

	def change_button_boarder_color(self):
		self.button_boarder_color = (255, 0, 0)
		
