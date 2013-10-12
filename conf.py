# your code goes here

MazeMap = [] 
fileread = []
x = []
y = []

with  open('configure','r') as f:
	
	for i in range(0,20):
		fileread.append(f.readline().strip("\n"))
f.close()
print fileread[19][9]
