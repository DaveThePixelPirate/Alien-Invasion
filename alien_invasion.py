import sys
import pygame

from settings import Settings
from ship import Ship
class AlienInvasion:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""init the game and create game resources"""
		#initializes the background settings needed for game to work
		pygame.init()

		#create settings object
		self.settings = Settings()
		#create a window using dimensiond from tuple (1200,800)
		# 1200 width, 800 height 
		#assigned to attribute self.screen so it can be available to everything in the class
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)



	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			#poll for events
			self._check_events()

			#redraw the screen during each pass through the loop
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()
			#make the most recenty drawn screen visible.
			pygame.display.flip()

	def _check_events(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

if __name__ == '__main__':
	#make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()