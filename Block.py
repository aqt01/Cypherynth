import pygame

class blocks(pygame.sprite.Sprite):

	def __init__(self,X,Y,dim,img):
		super(blocks, self).__init__()
		#pygame.sprite.Sprite.__init__(self)
		self.x = X
		self.y = Y
		self.image = img
		self.rect = img.get_rect()


	def get_img(self):
		return self.image