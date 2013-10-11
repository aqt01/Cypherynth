

import game
from random import randrange
import threading
import time
import game
import pygame
import Key

class Key(threading.Thread,pygame.sprite.Sprite):
	# recibe lista de tiburiones, posicion, velocidad y genero
	def __init__(self,key_lst,X,Y,dim,point,Map):#		self.Sharks_path = filename
		#threading.Thread.__init__(self)
		super(Key, self).__init__()
		self._stop = threading.Event()
		pygame.sprite.Sprite.__init__(self)
		#self.n = n #numero 
		
		self.x = X
		self.y= Y		
		
		self.map_x = point[0]
		self.map_y = point[1]

		self.maze_map = Map
		self.dimension = dimen
		self.alive = True
		self.opened = False
		self.vel = vel	
		self.img_pos = 0

		#self.Keys=[]
#		self.Fisheslist=[]
		self.type="key"
		#game.Collect_sprites()
		#SPRITES
		#self.spri = pygame.sprite.Sprite() # create sprite
		
		#self.topleft = [self.X, self.Y]
		self.key_lst = key_lst
		self.image = self.key_lst[0]
		self.image = pygame.transform.scale(self.image, (dim,dim))
		self.rect = self.image.get_rect() # use image extent values		
		self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		self.Or =2
	
		
	def get_img(self):
		return self.image

	def load_sprite(self,sprit_sharks,sprit_fishes):
		self.key_sprites = sprit_key
		self.block_sprites = sprit_block
		
	def Mov(self):
		""" OR = 0 : NORTE
		    OR = 1 : ESTE 
		    OR = 2 : SUR
		    OR = 3 : OESTE 
<<<<<<< HEAD
		"""
		self.rect.topleft = [self.x, self.y]

		if self.movd == self.dimension:
			self.movd =self.dimension/10
			if(self.map_x>0):
				if self.Or=0:
					if Map[self.map_x][self.map_y+1]==1:



			
		elif self.movd < self.dimension:
			self.movd +=2


			
		#self.Or = randrange(4)

		self.img_pos = self.Or+self.img_pos



		if (self.Or == 0):
			self.Y -= self.vel
				
		elif(self.Or == 1):
			self.x += self.vel
			elif (self.die==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][2]

			#elif(self.X>self.X_max_limit):
#				self.X=20
			#	self.X=X_max_limit-20
				

		elif (self.Or == 2):
			self.y += self.vel			
			
		elif(self.Or ==3):
			self.x -= self.vel
			
			elif(self.comer==1):
				self.comer=0
		
		self.image = self.shark_img_curr # load ball image
		self.rect = self.shark_img_curr.get_rect() # use image extent values			
		self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		
	def Draw(self):		
		self.screen.blit( self.shark_img_curr,(self.X, self.Y ))
	

	def Colision(self,objeto):
		if (objeto.type=="Block"):
			self.ChgOr()
		elif (objeto.type=="Lock"):
			self.Win()

	def Reproducir(self):
		print "Me reproduje"
		X=self.X 
		Y= self.Y
		g=randrange(2)
		shark=Sharks(self.shark_lst,X,Y,self.vel,g,self.X_max_limit,self.Y_max_limit)
		game.Sharkslist.append(shark)
		game.Sharkslist[-1].start()
		#shark.start()

	def Comer(self,objeto):
		print "Comi"
#		self.comer=1
		self.fish_img_curr = self.fish_lst[self.Or +self.mov_p][2]		     
		#time.sleep(0.7)		
		objeto.Die()

	def Die(self):
		self.image = self.key_lst[1]
		self.alive=False
		self._stop.set()
	
	def Win(self):
		self.opened = True

	def run(self):
		print 'Im Key' + self.n +" , i will find you!"
		while self.alive==True:		
			self.Mov()
			time.sleep(vel)


"""	def Draw_Sharks(self):
		for i in range(1,self.N_self.Sharks) :
			self.screen.blit( self.Sharks_img[0][0],(self.N_self.Sharks_ListX[i], self.N_self.Sharks_ListY[i] ), self.Shark_area)
		#pygame.Surface.blit( self.Sharks_img (50,50))

	
"""
