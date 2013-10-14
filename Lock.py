import pygame
from random import randrange
import threading
import game
import time

class Lock(pygame.sprite.Sprite):

	def __init__(self,lock_img,X,Y):

		super(Lock, self).__init__()
		self._stop = threading.Event()
		pygame.sprite.Sprite.__init__(self)
		self.x = X
		self.y = Y
		self.locked = True
		self.img_pos = 0

		self.image = lock_img
		self.rect = self.image.get_rect() # use image extent values			
		self.rect.topleft = [self.x, self.y] # put the ball in the top left corner		
		self.type="lock"
		

	def unlocked(self):
		self.locked = False
		time.sleep(0.7)
		print "WIN"

	def get_img(self):
                return self.image
        


