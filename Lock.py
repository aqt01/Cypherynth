import pygame
<<<<<<< HEAD
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
		
=======

class Lock(pygame.sprite.Sprite):

	def __init__(self,X,Y,dim,img):
		super(Lock, self).__init__()
		#pygame.sprite.Sprite.__init__(self)
		self.x = X
		self.y = Y
		self.image = img
		self.image = pygame.transform.scale(self.image, (dim,dim))
		self.rect = img.get_rect()
		

	def get_img(self):
		return self.image
		
	
	def getClases(self,sprite):
		for a in self.listClases:
			if(a.X==sprite.x and a.Y==sprite.y):
				self.Colision(a)

>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452

	def unlocked(self):
		self.locked = False
		time.sleep(0.7)
		print "WIN"

<<<<<<< HEAD
	def get_img(self):
                return self.image
        

=======
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452

