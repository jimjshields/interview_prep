class Door(object):
	"""Represents a door."""

	color = 'brown'

	def __init__(self, number, status):
		self.number = number
		self.status = status

	@classmethod
	def knock(cls):
		print 'Knock!'

	@classmethod
	def paint(cls, color):
		cls.color = color

	def open(self):
		self.status = 'open'

	def close(self):
		self.status = 'closed'

# Simple inheritance example
class SecurityDoor(Door):
	color = 'gray'
	locked = True

	def open(self):
		if self.locked:
			return
		super(SecurityDoor, self).open() # Best not to use super

# Class attributes are still global/shared
sdoor = SecurityDoor(1, 'closed')
SecurityDoor.color is Door.color # => True
sdoor.color is Door.color # => True

# print sdoor.__dict__
# print sdoor.__class__.__dict__
# print Door.__dict__
# print SecurityDoor.__bases__

print sdoor.status
sdoor.open()
print sdoor.status
sdoor.locked = False
sdoor.open()
print sdoor.status