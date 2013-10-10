import pygame

class Lock(pygame.sprite.Sprite):

	def __init__(self,X,Y,dim,img):
		super(Lock, self).__init__()
		#pygame.sprite.Sprite.__init__(self)
		self.x = X
		self.y = Y
		self.image = img
		self.rect = img.get_rect()


	def get_img(self):
		return self.image
		
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


