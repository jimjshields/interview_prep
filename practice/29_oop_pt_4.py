# -*- coding: utf-8 -*-

a = 5
print type(a) # type of data that is pointed to
print hex(id(a)) # memory address of the data

a = 'five'
print type(a)
print hex(id(a)) # same variable, different memory address

# Python's type system:
# Strong: everything has a well-defined type and you can check it with the
# type() built-in function
# Dynamic: The type of the variable is not explicitly declared, and it
# changes w/ the content

# Simplest possible function

# What is a?
# A reference -> it accepts a reference and returns a reference
# This is a universal function — does the same thing regardeless of input
def echo(a):
	return a

print echo(5) # this function can take any type
print echo('five') # this is basic polymorphism

# Can trust the input to perform the action — if a has a defined __add__ function,
# it'll work
def sum(a, b):
	return a + b

print sum(4, 5)
print sum(3.6, 2)
print sum('a', 'b')

# Takeaway — polymorphism in Python based on delegation
# Basically, if a method is implemented for a class/type somewhere in the class
# hierarchy, it'll work
# This is duck typing — 'acting like' instead of 'being'

# Example — accepts a door variable that just has to define the given methods
class Room(object):
	def __init__(self, door):
		self.door = door

	def open(self):
		self.door.open()

	def close(self):
		self.door.close()

	def is_open(self):
		return self.door.is_open()

# One way to define the class for the door variable
class Door(object):
	def __init__(self):
		self.status = 'closed'

	def open(self):
		self.status = 'open'

	def close(self):
		self.status = 'closed'

	def is_open(self):
		return self.status == 'open'

# Another way to define it; both can be used equally well
class BooleanDoor(object):
	def __init__(self):
		self.status = True

	def open(self):
		self.status = True

	def close(self):
		self.status = False

	def is_open(self):
		return self.status

door = Door()
bool_door = BooleanDoor()
room = Room(door)
bool_room = Room(bool_door)

room.open()
print room.is_open()
room.close()
print room.is_open()

bool_room.open()
print bool_room.is_open()
bool_room.close()
print bool_room.is_open()
