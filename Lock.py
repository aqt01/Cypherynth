import pygame
from random import randrange
import threading
import game
import time

class Lock(pygame.sprite.Sprite):

	def __init__(self,lock_img,X,Y):

		pygame.sprite.Sprite.__init__(self)
		self.X = X
		self.Y = Y
		self.locked = True
		self.img_pos = 0

		self.image = self.lock_img
		self.rect = self.lock_img.get_rect() # use image extent values			
		self.rect.topleft = [self.X, self.Y] # put the ball in the top left corner		
		self.type="lock"
		
	def load_sprite(self,sprit_sharks,sprit_fishes):
		self.sprit_sharks = sprit_sharks
		self.sprit_fishes = sprit_fishes
	
	def getClases(self,sprite):
		for a in self.listClases:
			if(a.X==sprite.x and a.Y==sprite.y):
				self.Colision(a)

	def Colision(self,objeto):
		if (objeto.type=="lock"):
			self.unlocked()

	def unlocked(self):
		self.locked = False
		time.sleep(0.7)
		print "WIN"


