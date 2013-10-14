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
<<<<<<< HEAD
		
=======
		#self.n = n #numero 
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452
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
<<<<<<< HEAD
=======
		#game.Collect_sprites()
		#self.topleft = [self.X, self.Y]
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452
		self.key_lst = key_lst
		self.image = self.key_lst[0]
		self.image = pygame.transform.scale(self.image, (dim,dim))
		self.rect = self.image.get_rect() # use image extent values		
		self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		self.movd=self.vel
		self.win = False

<<<<<<< HEAD
		print "< Key spawned >"
		
=======
#		print self.Map
		print " <<<<<<<<<<<<<<<<<<< IM KEY MA NIGGA!!! >>>>>>>>>>>>>>>>>>>>>>>>"
		#print "X" ,self.map_x
		#print  "Y ",self.map_y

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
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452

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

<<<<<<< HEAD
		self.rect.topleft = [self.x, self.y]
		if (self.Map[self.map_x][self.map_y]==3):
			self.Win()
		
		if self.movd > self.dimension:
			self.movd =self.vel
			

=======
		self.rect.topleft = [self.x, self.y]		
#		print "X: ", self.map_x
#		print "Y: ", self.map_y
#		print "THIS ", self.Map[self.map_x][self.map_y]
		#print "mov ", self.movd
		#print "vel ", self.vel		
	#	print self.Map[self.map_y]
#		print "MAP!!!!! ",

#		print self.Map,
#		print "YMAP",
#		print self.Map[self.map_y],

		#		print "Or ", self.Or
#		print "this : ",self.Map[self.map_y][self.map_x] 
#		print "West: ",self.Map[self.map_y-1][self.map_x] 
#		print "East: ",self.Map[self.map_y+1][self.map_x]
#		print "North: ",self.Map[self.map_y][self.map_x+1]
#		print "South: ",self.Map[self.map_y][self.map_x-1]
		print 
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

			"""
			x = str(self.map_x) + ' ' + str(self.map_y-1) + ' ' + str(self.Map[self.map_x][self.map_y-1])
#			print x
			x = str(self.map_x+1) + ' ' + str(self.map_y) + ' ' + str(self.Map[self.map_x+1][self.map_y])
#			print x
			x = str(self.map_x) + ' ' + str(self.map_y+1) + ' ' + str(self.Map[self.map_x][self.map_y+1])
#			print x
			x = str(self.map_x-1) + ' ' + str(self.map_y) + ' ' + str(self.Map[self.map_x-1][self.map_y])
#			print x
			"""
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452
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
<<<<<<< HEAD
			
=======
			#print "X: ", self.map_x
			#print "Y: ", self.map_y

>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452
	
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
<<<<<<< HEAD
				time.sleep(0.05)
=======
				time.sleep(0.005)
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452
				self.Die()		

		else :
			self.movd = self.movd+self.vel

		#self.Or = randrange(4)

			
			if self.alive :
				if (self.Or == 0):
					self.y = self.y - self.vel
				
				elif(self.Or == 1):
					self.x = self.x + self.vel
<<<<<<< HEAD
#				
=======
#				elif (self.==1):
#					self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][2]

>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452
				elif (self.Or == 2):
					self.y = self.y + self.vel			
			
				elif(self.Or ==3):
					self.x = self.x - self.vel
<<<<<<< HEAD

=======
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452
			
		#	self.image = self.shark_img_curr # load ball image
		#	self.rect = self.shark_img_curr.get_rect() # use image extent values			
		#	self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		
#	def draw(self):	
#		game.Game.screen.blit( self.get_img,(self.x, self.y ))

	def get_sons(self):		
		return self.sons

	def get_sons_obj(self):
		self.sons = 0
		return self.sons_obj


	def Die(self):
		self.image = self.key_lst[1]		
<<<<<<< HEAD
		#print self.Map
		print " Key: I died  "
=======
		print self.Map
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452
		self.alive=False
		self.sons=0
		#self._stop.set()
	
	def Win(self):
		self.win = True
<<<<<<< HEAD
#		self.x = self.dimension*10
#		self.y = self.dimension*9
		self.image=self.key_lst[2]	
		print "Key: I win!! I Got you!"
		print self.Map
		time.sleep(0.3)
		self.alive=False
		self.sons=0
		#self._stop.set()
=======
		self.image=self.key_lst[2]
		print "WIN"
		time.sleep(0.3)
		self.alive=False
		self.sons=0
#		self._stop.set()
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452
	


	def run(self):
<<<<<<< HEAD
		print 'Key: Im Key' +" , i will find you!"
		while self.alive==True:		
			self.Mov()
			time.sleep(0.05)
=======
		print 'Im Key' +" , i will find you!"
		while self.alive==True:		
			self.Mov()
			time.sleep(0.01)
>>>>>>> ad74fee00dc88596d5196ba6a0e8795352eea452


"""	def Draw_Sharks(self):
		for i in range(1,self.N_self.Sharks) :
			self.screen.blit( self.Sharks_img[0][0],(self.N_self.Sharks_ListX[i], self.N_self.Sharks_ListY[i] ), self.Shark_area)
		#pygame.Surface.blit( self.Sharks_img (50,50))

	
"""
