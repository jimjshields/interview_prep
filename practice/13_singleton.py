# What is a Singleton design pattern?
# http://www.uml.org.cn/c++/pdf/DesignPatterns.pdf

# Intent: Ensure a class has only one instance, and provide a global point of access to it.

# Motivation: There are lots of cases where you want a single instance of a class.
	# Good solution - make the class responsible for keeping track of its sole instance.

# Applicability: There must be exactly one instance of a class, and it must be accessible to clients from a well-known access point.
	# When the sole instance should be extensible by subclassing, and clients should be able to use an extended instance w/o modifying their code.

# Benefits: 
# 1. Controlled access to the sole instance
# 2. Reduced name space
# 3. Permits refinement of operations and representation
# 4. Permits a variable number of instances
# 5. More flexible than class operations

# Implementation
# 1. Ensuring a unique instance
# keep reading next time

# Metaclass implementation - http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class MyClass(object):
	__metaclass__ = Singleton

x = MyClass()
y = MyClass()
print x
print y