"""
"""

from pygame.locals import *
import pygame

# Dimensions of image files used is 32x32
IMAGE_HEIGHT = 32
IMAGE_WIDTH  = 32

class Game:
	def __init__(self):
		pygame.init()

	def load(self,level):
		self.level  = level
		self.height = len(level)
		self.width  = len(level[0])

		self.screen = pygame.display.set_mode([self.width*IMAGE_WIDTH,self.height*IMAGE_HEIGHT])
		self.clock  = pygame.time.Clock()

		# load images needed to draw the screen
		self.player   = pygame.image.load('human.png').convert()
		self.brick    = pygame.image.load('brick.png').convert()
		self.ladder   = pygame.image.load('ladder.png').convert()
		self.treasure = pygame.image.load('treasure.png').convert()
		self.bomb     = pygame.image.load('bomb.png').convert()
		self.exit     = pygame.image.load('exit.png').convert()
		self.blank    = pygame.image.load('blank.png').convert()

	def render_player(self,x,y):
		location = [x*IMAGE_WIDTH, y*IMAGE_HEIGHT]
		self.screen.blit(self.player,location)

	def render_object(self,x,y):
		location = [x*IMAGE_WIDTH, y*IMAGE_HEIGHT]

		if self.level[y][x] == '#':
			self.screen.blit(self.brick,location)
		elif self.level[y][x] == '=':
			self.screen.blit(self.ladder,location)
		elif self.level[y][x] == '@':
			self.screen.blit(self.treasure,location)
		elif self.level[y][x] == '*':
			self.screen.blit(self.bomb,location)
		elif self.level[y][x] == 'X':
			self.screen.blit(self.exit,location)
		else:
			self.screen.blit(self.blank,location)

	def start(self):
		# draw the screen
		for y in range(self.height):
			for x in range(self.width):
				self.render_object(x,y)

				if self.level[y][x] == 'P':
					self.player_location = [x,y]
					print ("Player at ", x, y)
				elif self.level[y][x] == 'X':
					self.exit_location = [x,y]
					print ("Exit at ", x, y)

		done = False
		self.player_died = False

		while not done:
			pygame.event.pump()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True

			# draw what was under the player
			self.render_object(self.player_location[0], self.player_location[1])

			# move the player, if user pressed any keys
			keys = pygame.key.get_pressed()
			if (keys[K_RIGHT]):
				self.player_location[0] = self.player_location[0] + 1
			if (keys[K_LEFT]):
				self.player_location[0] = self.player_location[0] - 1
			if (keys[K_DOWN]):
				self.player_location[1] = self.player_location[1] + 1
			if (keys[K_UP]):
				self.player_location[1] = self.player_location[1] - 1

			self.render_player(self.player_location[0], self.player_location[1])

			# make sure player didn't run into anything

			# make sure player is in bounds, or else they died
			if self.player_location[0] < 0:
				self.player_died = True
			elif self.player_location[0] > self.width:
				self.player_died = True
			elif self.player_location[1] < 0:
				self.player_died = True
			elif self.player_location[1] > self.height:
				self.player_died = True

			if self.player_died:
				done = True
			
			pygame.display.flip()
			self.clock.tick(30)

		pygame.quit()

