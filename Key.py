import game
from random import randrange
import threading
import time
import pygame
import Key

class Key(threading.Thread,pygame.sprite.Sprite):
	# recibe lista de tiburiones, posicion, velocidad y genero
	def __init__(self,key_lst,X,Y,dim,point,Map,Or):#		self.Sharks_path = filename
		#threading.Thread.__init__(self)
		super(Key, self).__init__()
		self._stop = threading.Event()
		pygame.sprite.Sprite.__init__(self)
		self.x = X
		self.y= Y				
		self.Point = point
		self.Or = Or
		self.map_x = point[0]
		self.map_y = point[1]
		self.sons_obj =[]
		self.Map = Map
		self.sons =0
		self.dimension = dim
		self.alive = True
		self.vel = dim/10
		self.key_lst = key_lst
		self.image = self.key_lst[0]
		self.image = pygame.transform.scale(self.image, (dim,dim))
		self.rect = self.image.get_rect() # use image extent values		
		self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		self.movd=self.vel
		self.win = False

		print "< Key spawned >"
		

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
		if (self.Map[self.map_x][self.map_y]==3):
			self.Win()
		
		if self.movd > self.dimension:
			self.movd =self.vel
			
			self.Map[self.map_x][self.map_y]=4
			if (self.Or==0) :
				 self.map_x=self.map_x-1
				 self.Point[0]=self.map_x
				 self.Point[1]=self.map_y

			elif (self.Or==1):
				 self.map_y=self.map_y+1
				 self.Point[0]=self.map_x
				 self.Point[1]=self.map_y

			elif (self.Or==2 ):
				 self.map_x=self.map_x+1
				 self.Point[0]=self.map_x
				 self.Point[1]=self.map_y

			elif (self.Or==3 ) :
				 self.map_y=self.map_y-1
				 self.Point[0]=self.map_x
				 self.Point[1]=self.map_y
	
			if (self.Or==0 and self.Map[self.map_x-1][self.map_y]==0) :
				if self.Map[self.map_x][self.map_y+1]!=0:
					self.Or=1
				elif self.Map[self.map_x][self.map_y-1]!=0:
					self.Or=3
				else:
					self.Die()

			elif (self.Or==1 and self.Map[self.map_x][self.map_y+1]==0) :
				if self.Map[self.map_x-1][self.map_y]!=0:
					self.Or=0
				elif self.Map[self.map_x+1][self.map_y]!=0:
					self.Or=2
				else:
					self.Die()
		
			elif (self.Or==2 and self.Map[self.map_x+1][self.map_y]==0) :
				if self.Map[self.map_x][self.map_y+1]!=0:
					self.Or=1
				elif self.Map[self.map_x][self.map_y-1]!=0:
					self.Or=3
				else:
					self.Die()


			elif (self.Or==3 and self.Map[self.map_x][self.map_y-1]==0) :
				if self.Map[self.map_x-1][self.map_y]!=0:
					self.Or=0
				elif self.Map[self.map_x+1][self.map_y]!=0:
					self.Or=2
				else:
					self.Die()

					
				
			if self.Map[self.map_x][self.map_y]==5:	

				if (self.Map[self.map_x-1][self.map_y]==1):
					x = Key(self.key_lst,self.x-1,self.y,self.dimension,self.Point,self.Map,0)
					self.sons_obj.append(x)
					self.sons = self.sons+1

				if (self.Map[self.map_x][self.map_y+1]==1):
					x = Key(self.key_lst,self.x,self.y+1,self.dimension,self.Point,self.Map,1)
					self.sons_obj.append(x)
					self.sons = self.sons+1

				if (self.Map[self.map_x+1][self.map_y]==1):
					x = Key(self.key_lst,self.x+1,self.y,self.dimension,self.Point,self.Map,2)
					self.sons_obj.append(x)
					self.sons = self.sons+1

				if (self.Map[self.map_x][self.map_y-1]==1):
					x = Key(self.key_lst,self.x,self.y-1,self.dimension,self.Point,self.Map,3)
					self.sons_obj.append(x)
					self.sons = self.sons+1
					
				
				#TIME?
				time.sleep(0.05)
				self.Die()		

		else :
			self.movd = self.movd+self.vel

		#self.Or = randrange(4)

			
			if self.alive :
				if (self.Or == 0):
					self.y = self.y - self.vel
				
				elif(self.Or == 1):
					self.x = self.x + self.vel
				elif (self.Or == 2):
					self.y = self.y + self.vel			
			
				elif(self.Or ==3):
					self.x = self.x - self.vel
	def get_sons(self):		
		return self.sons

	def get_sons_obj(self):
		self.sons = 0
		return self.sons_obj


	def Die(self):
		self.image = self.key_lst[1]		
		#print self.Map
		print " Key: I died  "
		self.alive=False
		self.sons=0
		#self._stop.set()
	
	def Win(self):
		self.win = True
#		self.x = self.dimension*10
#		self.y = self.dimension*9
		self.image=self.key_lst[2]	
		print "Key: I win!! I Got you!"
		print self.Map
		time.sleep(0.3)
		self.alive=False
		self.sons=0
		#self._stop.set()
	


	def run(self):
		print 'Key: Im Key' +" , i will find you!"
		while self.alive==True:		
			self.Mov()
			time.sleep(0.05)
