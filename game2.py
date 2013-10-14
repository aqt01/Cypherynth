

import pygame
import Lock, Key
import thread
import time
import Block
from random import randrange
	
	
KeyList = []
BlockList = []
maze_map = []
maze = []



class Game:

	def __init__(self,h ,vel,dimen): # w = 800, h = 600
		#Se inicializa pygame
		self.read_conf_file()
		self.factor = 20
		self.maze_length = h*self.factor*dimen
		self.dimension = dimen
		self.game = pygame
		self.game.init()
		self. vel = vel
		self.x = 0
		self.y = 0
		self.key_x = 0
		self.key_y = 0

		# Se carga el path del background
		self.background_path ="./Images/sprites/Mario_blocks.png"
		self.Width = self.factor*self.dimension*h
		self.Heigth = self.factor*self.dimension*h

		# Se carga el fondo con w y h que son introducidas por parametros
		self.screen=pygame.display.set_mode( (self.Width,self.Heigth),0,32)
		# Se carga la imagen de fondo
		
		self.background = self.game.image.load(self.background_path).convert()
		self.background = pygame.transform.scale(self.background,(self.Width,self.Heigth))
		# Se asigna la velocidad que seran los px que los sprites caminaran por cada paso
			
		self.vel = vel
#e cargan las imagenes de tiburones y peces
		self.Sprites_img()
		self.img_pos = 0
		self.alpha = 128
		#self.Sharks_spri = pygame.sprite.Group()
		#self.Fishes_spri = pygame.sprite.Group()		
		self.Create_units()
		self.Key.start()
		#self.Collect_sprites()

	def read_conf_file(self):		
		f = open('configure','r')
		n=0
		while 1:
			line = f.readline()
			n = n +1
			print n
			if not line:
				break
			#for i in range(0,20):
			maze_map.append(line.strip("\n"))

		print maze_map[19][9]

# La funcion se encarga de ir colectando las imagenes en dos listas mientras estas se van moviendo durante la ejecucion
	def Collect_sprites(self):
		# Se vacean las imagenes ya cargadas para ir cargando las demas

		self.BlockList.empty()

		OtherBlockList=[]

		for i in range(self.Shark_n):	
			if Sharkslist[i].alive:
				otherlistshark.append(Sharkslist[i])
				self.Sharks_spri.add( Sharkslist[i])

		for j in otherlistshark:
			j.load_sprite(self.Sharks_spri,self.Fishes_spri)

		otherlistfish = []

		for i in range(self.Fishes_n):
			if Fisheslist[i].alive:
				
				otherlistfish.append(Fisheslist[i])
				self.Fishes_spri.add( Fisheslist[i])

		for j in otherlistfish:
			j.load_sprite(self.Sharks_spri,self.Fishes_spri)
				#self.Fishes[i].load_sprite(self.Sharks_spri,self.Fishes_spri)
				
		


	# Funcion para crear las unidades, tanto los peces como los tiburones

	def key_img_list(self):
		return self.key_lst

	def Create_units(self):
	
		self.Keys = []
		self.Blocks = []
		self.Keys_sprites = []
		self.tmp = []
		#for i in range (0,15):
			#x = Key.Key( self.key_img_list(), self.X, self.Y)
		
		#Creamos bloques en las posiciones del mapa
		count = 0 

		#we iterate one time to collect all the coordinates
		tmp_list = []

		for val in  maze_map:
			for i in range(0,20):						  	tmp_list.append(int(val[i]))
			maze.append(list(tmp_list))
			tmp_list = []

				
		for i in range(0,21):
			for j in range(0,20):
				if ( maze[i][j] == 0):
					self.screen.blit(self.block_img ,(self.x,self.y))						
					self.Blocks.append( Block.block( self.x, self.y,self.dimension,self.block_img) )
				if(maze[i][j] ==3):							self.Lock =  Lock.Lock( self.x, self.y,self.dimension,self.lock_img) 
				if ( maze[i][j] ==2):		

					self.key_x = i
					self.key_y = j 
					self.key_points = [self.key_x,self.key_y]
					self.Key = Key.Key( self.key_img_list(), self.x, self.y,self.dimension,self.key_points,maze)
				
				self.x=self.dimension+self.x-1			
			self.x=0
			self.y=self.dimension+self.y-1
			


		print "weey ",maze[0][9]
		
	


		#for i in range(0,self.maze_length):
			#key_lst.append(x)


	#	self.Collect_sprites()

		
#		for i in range(Shark_n): 
#			key_lst[i].start()

#		for i in range(Fishes_n):
#			#MODIFICADO
#			Fisheslist[i].start()

	#Imagenes de los peces
	# Se cargan las imagenes de los peces, el mismo proceso se repite con los tiburones
	def Sprites_img(self):
		
		self.sprites_path = "./Images/sprites/"
		self.lock_path = self.sprites_path + "Lock.png"
		self.key_path = self.sprites_path + "Key.png"
		self.block_path = self.sprites_path + "Block.png"
		self.die_path = self.sprites_path + "Die.png"
		self.win_path = self.sprites_path + "Win.png"
		
		self.key_lst = []

		#Se cargan las imagenes del pez varon

		self.lock_img =	self.game.image.load(self.lock_path).convert_alpha(self.background)
		
		self.key_lst = [	self.game.image.load(self.key_path).convert_alpha(self.background), self.game.image.load(self.die_path).convert_alpha(self.background), self.game.image.load(self.win_path).convert_alpha(self.background) ]
		
		self.block_img =	self.game.image.load(self.block_path).convert_alpha(self.background) 
	# Se transforma la imagen a la dimension introducida
		self.block_img = pygame.transform.scale(self.block_img, (self.dimension,self.dimension))


		self.sprites_img = [ self.lock_img,list( self.key_lst),self.block_img]

	def draw(self):
		self.screen.blit( self.background, (0,0) )
		#self.Collect_sprites()

		#for i in range(self.key_n):	

		count = 0
		countf=0

		"""
		for val1 in ( maze_map):
			if count>19:
				break
			for i in range(0,20):
				if ( val1[i] == "0"):
					self.screen.blit(self.block_img ,(self.x,self.y))						
					
				self.x=self.dimension+self.x-1
			self.x=0
			self.y=self.dimension+self.y-1
			count=count+1
		"""
#		for val in( maze_map):		
#			if (countf>19):
#				countf=0
#				break
		for i in self.Blocks:
			self.screen.blit(i.get_img() ,(i.x ,i.y))						
			self.screen.blit(self.Lock.get_img() , (self.Lock.x,self.Lock.y))
			self.screen.blit(self.Key.get_img() , (self.Key.x,self.Key.y))


def main():
	juego = Game(1,20) #Se recibe 1er parametro la cantidad de tiburones y 2do cantidad de peces,
				   # 3er y 4to parametro son anchura y altura

	while True: # Loop, el juego se ejecuta dentro de esta clausura

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Para salir del juego
				exit_game()
		juego.draw()# Para dibujjar los sprites del juego
		colisionDict =pygame.sprite.groupcollide(juego.Sharks_spri,juego.Fishes_spri, 0, 0) # Para capturar las colisiones entre
										# Tiburones y peces, devuelve un diccionario con colisiones
		if  colisionDict:
			colisiones=colisionDict.values()
			for i in colisiones:
				for j in i:
					j.Die()
				#print i
			
		pygame.display.update()

def proof():
	juego = Game(1,8,30) #Se recibe 1er parametro la cantidad de tiburones y 2do cantidad de peces,
				   # 3er y 4to parametro son anchura y altura
	print maze_map
	while True: # Loop, el juego se ejecuta dentro de esta clausura

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Para salir del juego
				exit_game()
		juego.draw()# Para dibujjar los sprites del juego
		pygame.display.update()


if __name__ == "__main__":
	proof()

