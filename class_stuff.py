class Daddy(object): # generic class
	def __init__(self):
		print("Dad is awake!")

	def prepare_meal(self, meal):
		print(f"Dad is cooking {meal}")



class Good_Kid(Daddy): # class inherits from Daddy
	def __init__(self):
		super().__init__() # and the functions from parent class
		print("The [good] kid is awake! (and hungry)")

	
class Bad_Kid(Daddy): # class inherits from Daddy
	def __init__(self):
		# didn't call the parent like they were supposed to! oof, no access to functions
		print("The [bad] kid is awake! (and hungry)")


class School(object): # generic class
	def __init__(self):
		print("The school is open")


class Teacher(Bad_Kid, School): # inherits from kid and school base classes
	def __init__(self):
		print("The teacher says it's time to eat!")
		super().__init__() # call the functions




object = Teacher() 
object.prepare_meal('lunch')
