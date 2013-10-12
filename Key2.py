

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
		self.Point = point
		self.map_x = point[1]
		self.map_y = point[0]
		self.Map = Map
		self.dimension = dim
		self.alive = True
		self.opened = False
		self.vel = 2
		self.img_pos = 0
		self.sons = []
		self.type="key"
		#game.Collect_sprites()
		#self.topleft = [self.X, self.Y]
		self.key_lst = key_lst
		self.image = self.key_lst[0]
		self.image = pygame.transform.scale(self.image, (dim,dim))
		self.rect = self.image.get_rect() # use image extent values		
		self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		self.movd=0
#		print self.Map
		print "HELLO " ,self.map_x
		print  "HELLO ",self.map_y
	
		if (self.Map[self.map_x][self.map_y+1]==1):
			self.Or=2
		elif (self.Map[self.map_x][self.map_y-1]==1):
			self.Or=0
		elif (self.Map[self.map_x+1][self.map_y]==1):
			self.Or=1
		elif (self.Map[self.map_x-1][self.map_y-1]==1):
			self.Or=3
		
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
		#Create
		print "X: ", self.map_x
		print "Y: ", self.map_y
		print "mov ", self.movd
		print "vel ", self.vel
		print "Or ", self.Or
		print "West: ",self.Map[self.map_x-1][self.map_y] 
		print "East: ",self.Map[self.map_x+1][self.map_y]
		print "North: ",self.Map[self.map_x][self.map_y+1]
		print "South: ",self.Map[self.map_x][self.map_y-1]
	
		print "dimension ", self.dimension/10


		
		if self.movd > self.dimension:
			self.movd =self.dimension/10
			print "moVED"
			print "X: ", self.map_x
			print "Y: ", self.map_y
			print "mov ", self.movd
			print "vel ", self.vel
			print "9 2", self.Map[9][2]
			print "9 3", self.Map[9][3]
			print "9 1 ", self.Map[9][1]
					
			if (self.Or==0) :
				 self.map_y=self.map_y-1
				 self.Point[0]=self.map_y
				 self.Point[1]=self.map_x

			if (self.Or==1):
				 self.map_x=self.map_x+1
				 self.Point[0]=self.map_y
				 self.Point[1]=self.map_x

			if (self.Or==2 ):
				 self.map_y=self.map_y+1
				 self.Point[0]=self.map_y
				 self.Point[1]=self.map_x

			if (self.Or==3 ) :
				 self.map_x=self.map_x-1
				 self.Point[0]=self.map_y
				 self.Point[1]=self.map_x
			print "X: ", self.map_x
			print "Y: ", self.map_y

	
			if(self.map_x>0):
				if (self.Or==0 and self.Map[self.map_x][self.map_y-1]==0) :
					self.Die()
				if (self.Or==1 and self.Map[self.map_x+1][self.map_y]==0) :
					self.Die()
				if (self.Or==2 and self.Map[self.map_x][self.map_y+1]==0) :
					self.Die()
				if (self.Or==3 and self.Map[self.map_x-1][self.map_y]==0) :
					self.Die()
				self.Map[self.map_x][self.map_y]=4

				if self.Or==0:			
					if (self.Map[self.map_x+1][self.map_y]==1 and (self.Map[self.map_x][self.map_y-1]==4 or self.Map[self.map_x][self.map_y+1]==1 ) ): 
						x = self.Key(self.key_lst,self.x+self.dimension,self.y,self.dimension,self.Point,self.maze_map)
						self.sons.append(x)
					if  ( self.Map[self.map_x-1][self.map_y]==1 and (self.Map[self.map_x][self.map_y-1]==4 or self.Map[self.map_x][self.map_y+1]==1 ) ):
						x = self.Key(self.key_lst,self.x-self.dimension,self.y,self.dimension,self.Point,self.maze_map)
						self.sons.append(x)
				if self.Or==2:			
					if (self.Map[self.map_x+1][self.map_y]==1 and (self.Map[self.map_x][self.map_y-1]==1 or self.Map[self.map_x][self.map_y+1]==4 ) ): 
						x = self.Key(self.key_lst,self.x+self.dimension,self.y,self.dimension,self.Point,self.maze_map)
						self.sons.append(x)
					if  ( self.Map[self.map_x-1][self.map_y]==1 and (self.Map[self.map_x][self.map_y-1]==1 or self.Map[self.map_x][self.map_y+1]==4 ) ):
						x = self.Key(self.key_lst,self.x-self.dimension,self.y,self.dimension,self.Point,self.maze_map)
						self.sons.append(x)
					
				
				if (self.Or==1 ):
					if  ( ( self.Map[self.map_x][self.map_y-1]==1 ) and (self.Map[self.map_x-1][self.map_y]==4 or self.Map[self.map_x+1][self.map_y]==1 ) ):
						x = self.Key(self.key_lst,self.x,self.y-self.dimension,self.dimension,self.Point,self.maze_map)
						self.sons.append(x)
					if  (( self.Map[self.map_x][self.map_y+1]==1) and (self.Map[self.map_x-1][self.map_y]==4 or self.Map[self.map_x+1][self.map_y]==1 )) : 
						x = self.Key(self.key_lst,self.x,self.y+self.dimension,self.dimension,self.Point,self.maze_map)
						self.sons.append(x)
						
				if (self.Or==3 ):
					if  ( ( self.Map[self.map_x][self.map_y-1]==1 ) and (self.Map[self.map_x-1][self.map_y]==1 or self.Map[self.map_x+1][self.map_y]==4 ) ):
						x = self.Key(self.key_lst,self.x,self.y-self.dimension,self.dimension,self.Point,self.maze_map)
						self.sons.append(x)
					if  (( self.Map[self.map_x][self.map_y+1]==1) and (self.Map[self.map_x-1][self.map_y]==1 or self.Map[self.map_x+1][self.map_y]==4 )) : 
						x = self.Key(self.key_lst,self.x,self.y+self.dimension,self.dimension,self.Point,self.maze_map)
						self.sons.append(x)
					
				for i in self.sons:
					i.start()
		
		else :
			self.movd = self.movd+self.dimension/10

		#self.Or = randrange(4)

		
		if self.alive :
			if (self.Or == 0):
				self.y = self.y- self.mov
				
			elif(self.Or == 1):
				self.x = self.x +self.vel
#				elif (self.==1):
#					self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][2]

			elif (self.Or == 2):
				self.y = self.y+ self.vel			
			
			elif(self.Or ==3):
				self.x = self.x - self.vel
			
			elif(self.comer==1):
				self.comer=0
		
		#	self.image = self.shark_img_curr # load ball image
		#	self.rect = self.shark_img_curr.get_rect() # use image extent values			
		#	self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		
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
		print 'Im Key' +" , i will find you!"
		while self.alive==True:		
			self.Mov()
			time.sleep(0.1)


"""	def Draw_Sharks(self):
		for i in range(1,self.N_self.Sharks) :
			self.screen.blit( self.Sharks_img[0][0],(self.N_self.Sharks_ListX[i], self.N_self.Sharks_ListY[i] ), self.Shark_area)
		#pygame.Surface.blit( self.Sharks_img (50,50))

	
"""
