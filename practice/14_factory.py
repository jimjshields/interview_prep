# Factory design pattern

# http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Factory.html

import random

class Shape(object):
	"""A new shape."""

	pass

def factory(type):
	"""Creates a new shape object based on the class name."""

	class Circle(Shape):
		"""A new circle."""

		def draw(self):
			print 'Circle.draw'

		def erase(self):
			print 'Circle.erase'

	class Square(Shape):
		"""A new square."""

		def draw(self):
			print 'Square.draw'

		def erase(self):
			print 'Square.erase'


	if type == 'Circle':
		return Circle()
	elif type == 'Square':
		return Square()
	assert 0, 'Bad shape creation: {}'.format(type)

# Generate shape name strings
def shape_name_gen(n):
	for i in range(n):
		yield factory(random.choice(['Circle', 'Square']))

for shape in shape_name_gen(10):
	shape.draw()
	shape.erase()