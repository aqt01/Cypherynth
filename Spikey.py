import pygame

class spikey(pygame.sprite.Sprite):

	def __init__(self,X,Y,dim):
		super(spikey, self).__init__()
		#pygame.sprite.Sprite.__init__(self)
		self.x = X
		self.y = Y
		self.image = pygame.image.load("./Images/sprites/Spikey.png")
		self.image = pygame.transform.scale(self.image, (dim,dim))
		
		self.rect = self.image.get_rect()


	def get_img(self):
		return self.image
