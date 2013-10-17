import pygame
import Lock, Key
import thread
import time
import Block
import string
from random import randrange
	
	
BlockList = []
maze_map = []
maze = []


def Read_conf_file():
		conf = []
		all=string.maketrans('','')
		nodigs=all.translate(all, string.digits)
		f = open('configure.txt','r')		
		while 1:
				line = f.readline()			    
				if not line:
											break
				conf.append(line.translate(all, nodigs))
		return conf


# Contiene todas las llaves creadas
# Lectura de archivo de configuracion
# Devuelve lista con archivos donde, 0 tiburones, 1 peces, 2 anchura, 3 altura
		
class Game:
	def __init__(self,w,h ,vel,dimen): 
# Contiene todas las llaves creadas

		#Se inicializa pygame
		self.Read_conf_file()
		self.factor = 20
		self.key_list=[]
		self.Solution_lst = []
		self.Spikey_lst = []
		self.maze_length = h*self.factor*dimen
		self.dimension = dimen
		self.game = pygame
		self.game.init()
		self. vel = vel
		self.x = 0
		self.y = 0
		self.key_x = 0
		self.key_y = 0
		self.sons =0
		self.sons_obj= []

		# Se carga el path del background
		self.background_path ="./Images/sprites/Mario_blocks.png"
		self.Width = w
		self.Heigth = h

		# Se carga el fondo con w y h que son introducidas por parametros
		self.screen=pygame.display.set_mode( (self.Width,self.Heigth),0,32)
			# Se carga la imagen de fondo
		
		self.background = self.game.image.load(self.background_path).convert()
		self.background = pygame.transform.scale(self.background,(self.Width,self.Heigth))
		# Se asigna la velocidad que seran los px que los sprites caminaran por cada paso
			
		self.vel = vel
		#Se cargan las imagenes de tiburones y peces
		self.Sprites_img()
		self.img_pos = 0
		self.alpha = 128
		self.Create_units()
		self.Key.start()

# La funcion se encarga de ir colectando las imagenes en dos listas mientras estas se van moviendo durante la ejecucion
        
        def Read_conf_file(self):       
                f = open('Map.txt','r')               
                while 1:
                    line = f.readline()
                    if not line:
                        break
                    maze_map.append(line.strip("\n"))

    
	# Funcion para crear las unidades, tanto los peces como los tiburones

	def Create_units(self):
	
		self.Keys = []
		self.Blocks = []
		self.tmp = []
		
		#Creamos bloques en las posiciones del mapa
		count = 0 

		#we iterate one time to collect all the coordinates
		tmp_list = []

		for val in  maze_map:
			for i in range(0,21):						  	
				tmp_list.append(int(val[i]))
			maze.append(list(tmp_list))
			tmp_list = []

				
		for i in range(0,21):
			for j in range(0,20):
				if ( maze[i][j] == 0):
					self.screen.blit(self.block_img ,(self.x,self.y))						
					self.Blocks.append( Block.block( self.x, self.y,self.dimension,self.block_img) )
				if(maze[i][j] ==3):
					self.Lock =  Lock.Lock( self.lock_img,self.x, self.y) 
				if ( maze[i][j] ==2):
					self.key_x = i
					self.key_y = j 
					self.key_points = [self.key_x,self.key_y,2]
					self.Key = Key.Key( self.Key_img_list(), self.x, self.y,self.dimension,self.key_points,maze,2)					
					self.key_list.append(self.Key)	
				self.x=self.dimension+self.x			
			self.x=0
			self.y=self.dimension+self.y
			


		print "weey ",maze[0][9]
		
	#Imagenes de los peces
	# Se cargan las imagenes de los peces, el mismo proceso se repite con los tiburones
	#def Draw_key(self, img,coord,):
	#	self.screen.blit(img , (coord[0],coord[1]) )
	

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

		self.win_img = self.game.image.load(self.win_path).convert_alpha(self.background)
		self.win_img = pygame.transform.scale(self.win_img, (self.dimension,self.dimension))
		self.key_lst = [	self.game.image.load(self.key_path).convert_alpha(self.background), self.game.image.load(self.die_path).convert_alpha(self.background), self.win_img ]
		
		self.block_img =	self.game.image.load(self.block_path).convert_alpha(self.background) 
				# Se transforma la imagen a la dimension introducida
		self.block_img = pygame.transform.scale(self.block_img, (self.dimension,self.dimension))


		self.sprites_img = [ self.lock_img,list( self.key_lst),self.block_img]

	def Key_img_list(self):
		return self.key_lst
	def Draw(self):
		self.screen.blit( self.background, (0,0) )
		
		self.screen.blit(self.Lock.get_img() , (self.Lock.x,self.Lock.y))
		
		for j in self.Solution_lst:
			self.screen.blit(j.get_img() ,(j.x ,j.y))
			if j.is_spikey() :
				z = j.get_spikey()
				self.Spikey_lst.append(z)

		for k in self.Spikey_lst:
			self.screen.blit(k.get_img() ,(k.x ,k.y))
		
		for i in self.Blocks:
			self.screen.blit(i.get_img() ,(i.x ,i.y))		
		for i in self.key_list:			
			if i.Did_win():
				z = i.Call_solution()
				self.Solution_lst.append(z)
				self.Solution_lst[-1].start()

			if i.get_sons()>0:
				self.sons =  self.sons + i.get_sons()
				y = i.get_sons_obj()

				for j in y:
					self.key_list.append(j)
					time.sleep(0.1)
					self.key_list[-1].start()

			self.screen.blit(i.get_img() ,(i.x ,i.y))				
	
				


def main():

	conf = Read_conf_file()
	print conf
	juego = Game(int(conf[0]),int(conf[1]),int(conf[2]),int(conf[3])) #Se recibe 1er parametro la cantidad de tiburones y 2do cantidad de peces,
	print maze_map
	while True: # Loop, el juego se ejecuta dentro de esta clausura

		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Para salir del juego
				exit_game()
		juego.Draw()# Para dibujar los sprites del juego
		pygame.display.update()


if __name__ == "__main__":
	main()

