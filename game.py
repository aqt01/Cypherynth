import pygame
import Lock, Sharks
import thread
import time
from random import randrange
	

	
KeyList = []
BlockList = []
maze_map = []

class Game:

	def __init__(self,w,h, vel,dimen): # w = 800, h = 600
		#Se inicializa pygame
		self.read_conf_file()
		self.maze_length = h/dimen
		self.dimension = dimen
		self.game = pygame
		self.game.init()
		self. vel = vel
		self.x = 0
		self.y = 0
		# Se carga el path del background
		self.background_path ="./Images/sprites/Mario_blocks.png"
		self.Width = w
		self.Heigth = h	

		# Se carga el fondo con w y h que son introducidas por parametros
		self.screen=pygame.display.set_mode( (w,h),0,32)
		# Se carga la imagen de fondo
		
		self.background = self.game.image.load(self.background_path).convert()
		self.background = pygame.transform.scale(self.background,(w,h))
		# Se asigna la velocidad que seran los px que los sprites caminaran por cada paso
			
		self.vel = vel
		#se cargan las imagenes de tiburones y peces
		self.Sprites_img()
		self.img_pos = 0
		self.alpha = 128
		#self.Sharks_spri = pygame.sprite.Group()
		#self.Fishes_spri = pygame.sprite.Group()		
#		self.Create_units()
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
			for i in range(0,20):
				maze_map.append(line.strip("\n"))

		print maze_map[19][9]

# La funcion se encarga de ir colectando las imagenes en dos listas mientras estas se van moviendo durante la ejecucion
	def Collect_sprites(self):
		# Se vacean las imagenes ya cargadas para ir cargando las demas

		self.Sharks_spri.empty()
		otherlistshark=[]

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

	def Key_img_list(self):
		return self.key_lst

	def Create_units(self):
		
		
		self.Keys = []
		self.Keys_sprites = []
		
		for i in range (key_n):
			x = Key.Key( self.key_img_list(), self.X, self.Y)

		key_lst.append(x)


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
		#	if key_lst[i].alive == True:		
		#		self.screen.blit( key_lst[i].get_curr_img() ,(key_lst[i].X, key_lst[i].Y ))
		self.x=0
		self.y=0

		for val,i in enumerate( maze_map):
			for val1,j in enumerate( maze_map):
				if ( i[val1] == '0'):
					self.screen.blit(self.block_img ,(self.x,self.y))
					
				print val1, j[9]
				self.x=self.dimension+self.x-1
			if ( i == '0'):
				self.screen.blit(self.block_img ,(self.x,self.y))
					
			self.y=self.dimension+self.y-1
	

def main():
	juego = Game(600,600,20) #Se recibe 1er parametro la cantidad de tiburones y 2do cantidad de peces,
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
			print "Pez Choco Con tiburon"
		pygame.display.update()

def proof():
	juego = Game(600,600,8,20) #Se recibe 1er parametro la cantidad de tiburones y 2do cantidad de peces,
				   # 3er y 4to parametro son anchura y altura

	while True: # Loop, el juego se ejecuta dentro de esta clausura

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Para salir del juego
				exit_game()
		juego.draw()# Para dibujjar los sprites del juego
		pygame.display.update()


if __name__ == "__main__":
	proof()

