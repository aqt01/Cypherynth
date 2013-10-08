import pygame
import Fishes, Sharks
import thread
import time
from random import randrange
	

	
Sharkslist = []
Fisheslist = []

class Game:

	def __init__(self, Shark_n, Fishes_n,w,h): # w = 800, h = 600
		#Se inicializa pygame
		self.game = pygame
		self.game.init()
		# Se carga el path del background
		self.background_path ="./Images/background.jpg"
		self.Width = w
		self.Heigth = h		
		# Se carga el fondo con w y h que son introducidas por parametros
		self.screen=pygame.display.set_mode( (w,h),0,32)
		# Se carga la imagen de fondo
		self.background = self.game.image.load(self.background_path).convert()
		# Se asigna la velocidad que seran los px que los sprites caminaran por cada paso
		self.vel = 8
		#se cargan las imagenes de tiburones y peces
		self.Sharks_img()
		self.Fishes_img()
		
		self.img_pos = 0
		self.alpha = 128
		self.Sharks_spri = pygame.sprite.Group()
		self.Fishes_spri = pygame.sprite.Group()		
		self.Create_units(Shark_n,Fishes_n,self.vel)
		self.Collect_sprites()

		
	# La funcion se encarga de ir colectando las imagenes en dos listas mientras estas se van moviendo durante la ejecucion
	def Collect_sprites(self):
		# Se vacean las imagenes ya cargadas para ir cargando las demas

		self.Sharks_spri.empty()
		self.Fishes_spri.empty()
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

	def Create_units(self,Shark_n,Fishes_n,vel):
		self.pos = [] 
		self.vel = vel
		self.Shark_n = Shark_n
		self.Fishes_n = Fishes_n
		self.Sharks = []
		self.Fishes = []		
		self.Sharks_sprites = []
		self.Fishes_sprites = []

		


		for i in range (Shark_n):
			if i >= Shark_n/2:
				g=0
			else:
				g=1
			x = Sharks.Sharks( self.Retrieve_shark_lst(), randrange(self.Width), randrange(self.Heigth),self.vel,  g,self.Width,self.Heigth)
			#MODIFICADO
			Sharkslist.append(x)

		
		for i in range (Fishes_n):
			if i >= Fishes_n/2:
				g=0
			else:
				g=1

			y = Fishes.Fishes(self.Retrieve_fish_lst(), randrange(self.Width),randrange(self.Heigth), self.vel, g,self.Width,self.Heigth)

			#MODIFICADO
			Fisheslist.append(y)


		self.Collect_sprites()

		
		for i in range(Shark_n):
			#MODIFICADO
			Sharkslist[i].start()

		for i in range(Fishes_n):
			#MODIFICADO
			Fisheslist[i].start()

	#Imagenes de los peces
	# Se cargan las imagenes de los peces, el mismo proceso se repite con los tiburones
	def Sprites_img(self):
		
		self.sprites_path = "./Images/sprites/"
		self.lock_path = self.sprites_path + "Lock.png"
		self.key_path = self.sprites_path + "Key.png"
		self.block_path = self.sprites_path + "Block.png"

		#Se cargan las imagenes del pez varon

		self.lock_img =	self.game.image.load(self.lock_path).convert_alpha(self.background))
		self.key_img =	self.game.image.load(self.key_path).convert_alpha(self.background) )
		self.block_img =	self.game.image.load(self.block_path).convert_alpha(self.background) )

		

		self.sprites_img = [ lock_img,key_img,block_img]

	def draw(self):
		self.screen.blit( self.background, (0,0) )

		self.Collect_sprites()

		for i in range(self.Shark_n):	
			if Sharkslist[i].alive == True:
				#MODIFICADO
				self.screen.blit( Sharkslist[i].get_curr_img() ,(Sharkslist[i].X, Sharkslist[i].Y ))


		for j in range(self.Fishes_n):
			if Fisheslist[j].alive == True:
				self.screen.blit( Fisheslist[j].get_curr_img() ,(Fisheslist[j].X, Fisheslist[j].Y ))

	

def main():
	juego = Game(10,40,800,600) #Se recibe 1er parametro la cantidad de tiburones y 2do cantidad de peces,
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

if __name__ == "__main__":
	main()

