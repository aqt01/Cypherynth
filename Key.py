import game
from random import randrange
import threading
import time
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
		self.Or = point[2]
		self.map_x = point[0]
		self.map_y = point[1]
		self.sons_elements =[]
		self.Map = Map
		self.KeyList=[]
		self.sons =0
		self.dimension = dim
		self.alive = True
		self.vel = dim/10
		self.type="key"
		#game.Collect_sprites()
		#self.topleft = [self.X, self.Y]
		self.key_lst = key_lst
		self.image = self.key_lst[0]
		self.image = pygame.transform.scale(self.image, (dim,dim))
		self.rect = self.image.get_rect() # use image extent values		
		self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		self.movd=self.vel
#		print self.Map
		print " <<<<<<<<<<<<<<<<<<< IM KEY MA NIGGA!!! >>>>>>>>>>>>>>>>>>>>>>>>"
		#print "HELLO " ,self.map_x
		#print  "HELLO ",self.map_y

		"""
		if (self.Map[self.map_x][self.map_y+1]==1):
			self.Or=2
		elif (self.Map[self.map_x][self.map_y-1]==1):
			self.Or=0
		elif (self.Map[self.map_x+1][self.map_y]==1):
			self.Or=1
		elif (self.Map[self.map_x-1][self.map_y-1]==1):
			self.Or=3
		"""

	def get_img(self):
		return self.image

	def load_sprite(self,sprit_sharks,sprit_fishes):
		self.key_sprites = sprit_key
		self.block_sprites = sprit_block
		
	def Mov(self):
	 	""" OR = 0 : NORTE
		    OR = 1 : ESTE 
		    OR = 2 : SUR
		    OR = 3 : OESTE """

		self.rect.topleft = [self.x, self.y]		
		print "X: ", self.map_x
		print "Y: ", self.map_y
		#print "mov ", self.movd
		#print "vel ", self.vel
		print self.Map[self.map_y]
		print "Or ", self.Or
		print "this : ",self.Map[self.map_y][self.map_x] 
		print "West: ",self.Map[self.map_x-1][self.map_y] 
		print "East: ",self.Map[self.map_x+1][self.map_y]
		print "North: ",self.Map[self.map_x][self.map_y+1]
		print "South: ",self.Map[self.map_x][self.map_y-1]
		
		if (self.Map[self.map_x][self.map_y]==3):
			self.Win()
		#print "dimension ", self.dimension/10

		if self.movd > self.dimension:
			self.movd =self.vel
			#print "moVED"
			#print "X: ", self.map_x
			#print "Y: ", self.map_y
			#print "map ", self.Map[self.map_x][self.map_y]
			#print "mov ", self.movd
			#print "vel ", self.vel

			
			x = str(self.map_x) + ' ' + str(self.map_y-1) + ' ' + str(self.Map[self.map_x][self.map_y-1])
			print x
			x = str(self.map_x+1) + ' ' + str(self.map_y) + ' ' + str(self.Map[self.map_x+1][self.map_y])
			print x
			x = str(self.map_x) + ' ' + str(self.map_y+1) + ' ' + str(self.Map[self.map_x][self.map_y+1])
			print x
			x = str(self.map_x-1) + ' ' + str(self.map_y) + ' ' + str(self.Map[self.map_x-1][self.map_y])
			print x

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
				"""if (self.Or==0 and self.Map[self.map_x][self.map_y-1]==0) :
					self.Die()
				if (self.Or==1 and self.Map[self.map_x+1][self.map_y]==0) :
					self.Die()
				if (self.Or==2 and self.Map[self.map_x][self.map_y+1]==0) :
					self.Die()
				if (self.Or==3 and self.Map[self.map_x-1][self.map_y]==0) :
					self.Die()
					"""
				
				if self.Map[self.map_x][self.map_y]==5:	
					self.Map[self.map_x][self.map_y]=4
					if (self.Map[self.map_x][self.map_y-1]==1):
						self.Point[2] = 0
						x = [self.key_lst,self.x,self.y-self.dimension,self.dimension,self.Point,self.Map]
						self.sons_elements.append(x)
						self.sons = self.sons+1

					if (self.Map[self.map_x+1][self.map_y]==1):
						self.Point[2] = 1
						x = [self.key_lst,self.x+self.dimension,self.y,self.dimension,self.Point,self.Map]
						self.sons_elements.append(x)
						self.sons = self.sons+1

					if (self.Map[self.map_x][self.map_y+1]==1):
						self.Point[2] = 2
						x = [self.key_lst,self.x,self.y+self.dimension,self.dimension,self.Point,self.Map]
						self.sons_elements.append(x)
						self.sons = self.sons+1

					if (self.Map[self.map_x-1][self.map_y]==1):
						self.Point[2] = 3
						x = [self.key_lst,self.x-self.dimension,self.y,self.dimension,self.Point,self.Map]
						self.sons_elements.append(x)
						self.sons = self.sons+1
					
					for i in self.KeyList:
						i.start()
				

					self.Die()		

		else :
			self.movd = self.movd+self.vel

		#self.Or = randrange(4)

			
			if self.alive :
				if (self.Or == 0):
					self.y = self.y - self.vel
				
				elif(self.Or == 1):
					self.x = self.x + self.vel
#				elif (self.==1):
#					self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][2]

				elif (self.Or == 2):
					self.y = self.y + self.vel			
			
				elif(self.Or ==3):
					self.x = self.x - self.vel
			
				elif(self.comer==1):
					self.comer=0
		#	self.image = self.shark_img_curr # load ball image
		#	self.rect = self.shark_img_curr.get_rect() # use image extent values			
		#	self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		
#	def draw(self):	
#		game.Game.screen.blit( self.get_img,(self.x, self.y ))

	def get_sons(self):		
		return self.sons

	def get_sons_elements(self):
		self.sons = 0
		return self.sons_elements


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
		print self.Map
		self.alive=False
		self._stop.set()
	
	def Win(self):
		self.opened = True

	def run(self):
		print 'Im Key' +" , i will find you!"
		while self.alive==True:		
			self.Mov()
			time.sleep(0.2)


"""	def Draw_Sharks(self):
		for i in range(1,self.N_self.Sharks) :
			self.screen.blit( self.Sharks_img[0][0],(self.N_self.Sharks_ListX[i], self.N_self.Sharks_ListY[i] ), self.Shark_area)
		#pygame.Surface.blit( self.Sharks_img (50,50))

	
"""
