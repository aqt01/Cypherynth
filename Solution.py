
from random import randrange
import threading
import time
import pygame
import copy
import Spikey

class Solution_finder(threading.Thread,pygame.sprite.Sprite):
	# recibe lista de tiburiones, posicion, velocidad y genero
	def __init__(self,dim,Map):#		self.Sharks_path = filename
		#threading.Thread.__init__(self)
		super(Solution_finder, self).__init__()
		self._stop = threading.Event()
		pygame.sprite.Sprite.__init__(self)
		self.x = dim*9
		self.y = 0				
		self.Or = 2
		self.map_x = 0
		self.map_y = 9		
		self.Map = copy.deepcopy(Map)
		self.sons =0
		self.dimension = dim
		self.alive = True
		self.vel = dim/10
		self.image = pygame.image.load("./Images/sprites/Solution.png") 
		self.image = pygame.transform.scale(self.image, (dim,dim))		
		#self.spikey_lst = []		
		self.spikey_available = False


		self.rect = self.image.get_rect() # use image extent values		
		self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
		self.movd=self.vel
		self.finded = False

		print "< Solution spawned >"
		

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
			self.Finded()
		
		if self.movd > self.dimension:
			self.movd =self.vel
			
			self.spikey= Spikey.spikey(self.x,self.y,self.dimension)
			self.spikey_available = True

			if (self.Or==0) :
				 self.map_x=self.map_x-1
			elif (self.Or==1):
				 self.map_y=self.map_y+1
			elif (self.Or==2 ):
				 self.map_x=self.map_x+1

			elif (self.Or==3 ) :
				 self.map_y=self.map_y-1
	
			if (self.Or==0 and self.Map[self.map_x-1][self.map_y]!=4) :
				if self.Map[self.map_x][self.map_y+1]==4 or self.Map[self.map_x][self.map_y+1]==3 : 
					self.Or=1
				elif self.Map[self.map_x][self.map_y-1]==4 or self.Map[self.map_x][self.map_y-1]==3 :
					self.Or=3

			elif (self.Or==1 and self.Map[self.map_x][self.map_y+1]!=4) :
				if self.Map[self.map_x-1][self.map_y]==4 or self.Map[self.map_x-1][self.map_y]==3: 
					self.Or=0
				elif self.Map[self.map_x+1][self.map_y]==4 or self.Map[self.map_x+1][self.map_y]==3:
					self.Or=2
		
			elif (self.Or==2 and self.Map[self.map_x+1][self.map_y]!=4) :
				if self.Map[self.map_x][self.map_y+1]==4 or self.Map[self.map_x][self.map_y+1]==3:
					self.Or=1
				elif self.Map[self.map_x][self.map_y-1]==4 or self.Map[self.map_x][self.map_y-1]==3:
					self.Or=3


			elif (self.Or==3 and self.Map[self.map_x][self.map_y-1]!=4) :
				if self.Map[self.map_x-1][self.map_y]==4 or self.Map[self.map_x-1][self.map_y]==3:
					self.Or=0
				elif self.Map[self.map_x+1][self.map_y]==4 or self.Map[self.map_x+1][self.map_y]==4 :
					self.Or=2

					
				#TIME?
				time.sleep(0.05)

		else :
			self.movd = self.movd+self.vel
			if self.spikey_available :
				self.spikey_available = False

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
	def get_spikey(self):		
		return self.spikey

	def is_spikey(self):
		return self.spikey_available

	def Finded(self):
		self.finded = True
		print "Lakitu: Solution finded"
		print self.Map
		time.sleep(0.3)
		self.alive=False
		self.sons=0
		self._stop.set()
	
	def run(self):
		print 'Lakitu: Im lakitu' +" , I' show you the solution!"
		while self.alive==True:		
			self.Mov()
			time.sleep(0.05)
