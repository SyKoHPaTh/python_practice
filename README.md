# Python Practice
# Github repository: https://github.com/SyKoHPaTh/python_practice
# A collection of small direct-functionality Python programs
# Not all files have video lessons, ones that do will include a link within the program

Python Basic Topics:
Installing Python (3.9.6) with PyGame (2.0.1) and SublimeText (4) - https://www.youtube.com/watch?v=3P_m3WO3lN8
	- Need to make an updated video covering current versions:
		- Python (3.10.7): https://www.python.org/downloads/
		- Pygame (2.1.2): pip install pygame
			- Windows, run CMD as Admin
		- SublimeText (4-build 4126): https://www.sublimetext.com/download

Python Requests
	- Web services; delete, get, head, patch, post, put, request
	- Can communicate with API's (typically JSON)

Importing modules
	- import <module>
		- from <module> import <variable>
	- import <module> as <name>
		- from <module> import <variable> as <name>

Variables & Math
	- Variable holds a value
		- All Python variables are Implicit unless you define them (Explicit), and are treated as such
			- var_integer = 123 # integer
			- var_float = 1.23 # float
			- var_string = "123" # string
		- can be typecast to change what they are: Explicit conversion
			- int(), float(), str()
	- Algebra: operations that change the values within variables
		- Basic operations: +, -, *, /
		- Other operators: **, %, //
	- math Module:
		- Constants:
			- pi, e, tau, inf, nan
		- Trigonometry:
			- cos, sin, tan
			- Angles: degrees, radians
		- Numbers:
			- ceil, floor, fabs

Functions
	- def <function_name>( <parameters> = <default_value>, ... ):
	- Arguments are passed to Function Parameters as copies, not by reference
	- Optional, can return a value
	- Recursive functions

Classes & Objects
	- class <name>:
		- Constructor __init__()
		- self.<variables>
			- def <function>(<self>)
	- var_object = <name>()

Data structures
	- lists, tuples, sets, dictionaries