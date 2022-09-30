import random

# ----- Functions -----
def print_grid(map_view):
	# Print out the Dungeon
	for y in range(dungeon_height):
		row = ''
		for x in range(dungeon_width):
			if map_view == True:
				cell = grid[x][y]
				if cell == 'o':
					if x < 20 and x > 0 and grid[x + 1][y] != 0 and grid[x - 1][y] != 0:
						cell = '-'
					else:
						cell = '|'
				if cell == 's':
					cell = '█' # secret
				if cell == 'b':
					cell = '▒' # bomb cracks
				if cell == 'O' or cell == 'K' or cell == 'P':
					cell = '░' # Open
				if cell == 0:
					cell = '█' # wall
				if cell == '>':
					cell = '→' # one way
				if cell == '<':
					cell = '←' # one way 
				if cell == '^':
					cell = '↑' # one way
				if cell == 'v':
					cell = '↓' # one way
				if cell == 'k' or cell == 'p':
					cell = 'Ð' # closed door
					

				row += cell
			else: # raw data
				row += str(grid[x][y])
		print(row)

def move_path(path_x, path_y, room_x, room_y, door_type, room_type, overwrite = False):
	if overwrite == False:
		# Path
			if grid[path_x][path_y] == 0:
				grid[path_x][path_y] = door_type
		# Room
			if grid[room_x][room_y] == 0:
				grid[room_x][room_y] = room_type
	else: # Places a door and path regardless of existing data
		# Path
			grid[path_x][path_y] = door_type
		# Room
			grid[room_x][room_y] = room_type


# ----- Main -----

dungeon_width = 21
dungeon_height = 21

grid = [[0 for x in range(dungeon_width)] for x in range (dungeon_height)] # Create 2D array (size is 13 x 13)

# Init the pen
room_x = 10
room_y = 20
grid[room_x][room_y] = "E"


# Draw the actual friggin dungeon
'''
	Rooms
	E		Entrance
	O		open room
	X		Boss
	A		Enemy "ambush" room (all "open" doors locked until enemies defeated)
	P		Puzzle room (solve to open door)
	I		special item (unique)
	K		Drop a key (clear all enemies, or if no enemies, just have on ground)
	M		Drop a map (clear all enemies, or if no enemies, just have on ground)
	B		Drop a bomb (clear all enemies, or if no enemies, just have on ground)

	Paths
	o		straight open door
	<>^v	one-way door (using <>^v for drawing purposes)
	k		locked (use key)
	b		cracked (use bomb)
	s		secret (push wall)
	p		puzzle	(solve puzzle)
'''
# Unique Rooms
unique_room_item = False;
unique_room_map = False;
keys = 0

difficulty = 6

for distance in range(100):
	move_choice = random.randrange(0, 4)
	door_choice = random.randrange(0, difficulty)
	room_choice = random.randrange(0, difficulty)
	path_x = room_x
	path_y = room_y
	overwrite = False

	# Door choice
	path_type = 'o'
	if door_choice == 0: # open 
		path_type = 'o'
	elif door_choice == 1 and keys > 0: # key
		path_type = 'k'
		keys -= 1
	elif door_choice == 2: # oneway
		path_type = 'W'
	elif door_choice == 3 and grid[room_x][room_y] == 'O' : # Puzzle (overwrites current room if clear)
		path_type = 'p'
		grid[room_x][room_y] = 'P'
		overwrite = True
	elif door_choice == 4: # cracked
		path_type = 'b'
	elif door_choice == 5: # secret
		path_type = 's'

	# Room Choice
	room_type = 'O'
	if room_choice == 0: # Open 
		room_type = 'O'
	if room_choice == 1: # Key
		room_type = 'K'
		keys += 1
	if room_choice == 2 and unique_room_item == False: # Item
		room_type = 'I'
		unique_room_item = True
		overwrite = True
	if room_choice == 3 and unique_room_map == False: # Map
		room_type = 'M'
		unique_room_map = True
		overwrite = True
	if room_choice == 4: # Bomb (can get them outside of maze, but w/e)
		room_type = 'B'
	if room_choice == 5: # enemy room
		room_type = 'A'

	if move_choice == 0 and room_y > 0 and grid[room_x][room_y - 1] != 'v': # Up
		if path_type == 'W':
			path_type = '^'
		path_y = room_y - 1
		room_y -= 2
		move_path(path_x, path_y, room_x, room_y, path_type, room_type, overwrite)
	elif move_choice == 1 and room_y < dungeon_height - 1 and grid[room_x][room_y + 1] != '^': # Down
		if path_type == 'W':
			path_type = 'v'
		path_y = room_y + 1
		room_y += 2
		move_path(path_x, path_y, room_x, room_y, path_type, room_type)
	elif move_choice == 2 and room_x > 0 and grid[room_x - 1 ][room_y] != '>': # Left
		if path_type == 'W':
			path_type = '<'
		path_x = room_x - 1
		room_x -= 2
		move_path(path_x, path_y, room_x, room_y, path_type, room_type)
	elif move_choice == 3 and room_x < dungeon_width - 1 and grid[room_x + 1][room_y] != '<': # Right
		if path_type == 'W':
			path_type = '>'
		path_x = room_x + 1
		room_x += 2
		move_path(path_x, path_y, room_x, room_y, path_type, room_type)


grid[room_x][room_y] = 'X'

print("All:")
print_grid(False)

print("Map:")
print_grid(True)


