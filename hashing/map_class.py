class Map(object):
	"""Represents a map/assoc. array/dictionary ADT."""

	def __init__(self):
		"""Initializes w/ an empty list of keys and empty list of values."""

		self.dict = {}

	def add_key_val_pair(self, key, val):
		"""Adds a key/value pair to the map. Replaces value if key already present."""

		self.dict[key] = val

	def get_val(self, key):
		"""Returns a value for a given key if available. Raises KeyError if not."""

		return self.dict[key]

	def remove_key(self, key):
		"""Deletes a key/value pair for a given key if available. Raises KeyError if not."""

		del self.dict[key]



# my_map.add_key_val_pair(1, 2)
# my_map.add_key_val_pair(1, 3)
# my_map.add_key_val_pair(1, 4)
# my_map.add_key_val_pair(3, 2)

# print my_map.dict

# print my_map.get_val(1)

# my_map.remove_key(3)

# print my_map.dict

class Map_2(object):
	"""Represents a map/assoc. array/dictionary ADT."""

	def __init__(self):
		"""Initializes w/ an empty list of keys and empty list of values."""

		self.keys = []
		self.values = []

	def add_key_val_pair(self, key, val):
		"""Adds a key/value pair to the map. Replaces value if key already present."""

		if key in self.keys:
			self.values[self.keys.index(key)] = val
		else:
			self.keys.append(key)
			self.values.append(val)

	def get_val(self, key):
		"""Returns a value for a given key if available. Raises KeyError if not."""

		return self.values[self.keys.index(key)]

	def remove_key(self, key):
		"""Deletes a key/value pair for a given key if available. Raises KeyError if not."""

		index = self.keys.index(key)
		del self.keys[index]
		del self.values[index]

# my_map_2.add_key_val_pair(1, 2)
# my_map_2.add_key_val_pair(1, 3)
# my_map_2.add_key_val_pair(1, 4)
# my_map_2.add_key_val_pair(3, 2)

# print zip(my_map_2.keys, my_map_2.values)

# print my_map_2.get_val(1)

# my_map_2.remove_key(3)

# print zip(my_map_2.keys, my_map_2.values)

from timeit import timeit
import random

my_map = Map()
for _ in xrange(10000):
	my_map.add_key_val_pair(''.join([chr(random.choice(list(xrange(97, 123)))) for _ in xrange(6)]), 1)

my_map_2 = Map_2()
for _ in xrange(10000):
	my_map_2.add_key_val_pair(''.join([chr(random.choice(list(xrange(97, 123)))) for _ in xrange(6)]), 1)

# print my_map.dict
# print zip(my_map_2.keys, my_map_2.values)
print timeit('for key in my_map.dict.keys(): my_map.get_val(key)', 'from __main__ import my_map', number=10)
print timeit('for key in my_map_2.keys: my_map_2.get_val(key)', 'from __main__ import my_map_2', number=10)