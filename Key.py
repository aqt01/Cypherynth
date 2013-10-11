

import game
from random import randrange
import threading
import time
import game
import pygame
import Key

class Key(threading.Thread,pygame.sprite.Sprite):
	# recibe lista de tiburiones, posicion, velocidad y genero
	def __init__(self,key_lst,X,Y,dim,vel,Map):#		self.Sharks_path = filename
		#threading.Thread.__init__(self)
		super(Key, self).__init__()
		self._stop = threading.Event()
		pygame.sprite.Sprite.__init__(self)
		#self.n = n #numero 
		self.x = X
		self.y= Y		
		self.maze_map = Map

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
		self.Or = randrange(0,4)
	
		count = 0 
		for val in ( self.maze_map):
			if count>20:
				break
			for i in range(0,20):
				if (val[i] =="2"):	
						self.key_x = count
						self.key_y = i 	
				print "klk!! " ,self.maze_map
		
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

		#print "Shark: ",self.rect.topleft

		if self.movd == 10:
			self.Or = randrange(0,4)	
			self.movd =0
		elif self.movd < 10:
			self.movd +=1


			
		#self.Or = randrange(4)

		self.img_pos = self.Or+self.img_pos



		if (self.Or == 0):
			self.Y -= self.vel
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][1]				
				self.mov_n=0
			
			elif(self.comer==1):
				self.comer=0
#			elif(self.Y>self.Y_max_limit):
##				self.Y=20				
				#self.Y=self.Y_max_limit-20
				
		elif(self.Or == 1):
			self.x += self.vel
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][1]				
				self.mov_n=0
			elif (self.die==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][2]

			elif(self.comer==1):
				self.comer=0
			#elif(self.X>self.X_max_limit):
#				self.X=20
			#	self.X=X_max_limit-20
				

		elif (self.Or == 2):
			self.y += self.vel			
			
		elif(self.Or ==3):
			self.x -= self.vel
			
			if(self.mov_n==0):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][0]
				self.mov_n =1
			elif (self.mov_n==1):
				self.shark_img_curr = self.shark_lst[self.Or +self.mov_p][1]				
				self.mov_n=0
				
			elif(self.comer==1):
				self.comer=0
		
#			elif(self.X<self.X_min_limit):
				##self.X=X_max_limit-20
				#self.X=20

		if(self.x>self.X_max_limit):				
				self.x=0
				self.movd=0
		elif(self.y<self.Y_min_limit):
				self.y=self.Y_max_limit
				self.movd=0
				#self.Y=20
		elif(self.y>self.Y_max_limit):
				self.Y=0
				self.movd=0				
				#self.Y=self.Y_max_limit-20
		elif(self.x<self.X_min_limit):
				self.x=self.X_max_limit
				self.movd=0
				#self.X=20

			#self.topleft = [self.X, self.Y]
		self.image = self.shark_img_curr # load ball image
		self.rect = self.shark_img_curr.get_rect() # use image extent values			
		self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
			#print "SPRITE: ", self.spri.rect
			#print "NOT SPRITE: ", self.X,self.Y

		
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
