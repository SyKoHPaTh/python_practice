''' 
Making a "GRID" for 2D tile-based games 

"GRID"  is a list of lists

2-Dimensional arrays are commonly used for maps in 2D games.
'''

width = 5 # x, horizontal
height = 7 # y, vertical

grid = [[]]  # This is not readable!  boo :(  And also NOT INITIALIZED

#grid[3][2] = 1   # This doesn't work because the grid hasn't been properly initialized

print(f"Before Initialization: {grid}") # before initialization

grid = [[0 for x in range(width)] for y in range (height)] # Initializes the grid, remember it's grid[width][height]
# Initialization means it sets values to a default we define (0), so when we try to access the cell, it already exists and doesn't give us an error when we try to access it
print(f"After Initialization {grid}")

# Remember that grid[height][width]: grid[y][x].  We're setting coordinates (2,3)=1
grid[3][2] = 1
# As you can see, this sets the third value of the fourth nested list, because lists start with 0
print(f"Set coordinate: {grid}")

# Since this is a list of lists, we need to iterate through them as such: grid[y][x]
	# note that the following code is an alternate way of accessing a grid such as the initialization above [[list in a] list]
for y in range(height):
	for x in range(width):
		print(f"x, y = {x},{y}  Value: {grid[y][x]}")  # Readable code has variables within the string, easier to read than: print("x,y: ", x, ", ", y)


'''
Further research: enums

'''