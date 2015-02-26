# Hashing: implementation of a mapping that can be operated on in O(1) time
# Most importantly: every item needs to be in a particular place
# Hashing function: maps the item (whatever it is) to a value that represents a place in the table - it's already there (called a slot)

# Hash table: collection of items which are stored so that they're easy to find later
# Modulo - typically present in hash functions as the result must be in the range of slot names

# Load factor: number of items / table size
# Can stay at O(1) time if each item maps to a unique location in the hash table
# But often they can't - this leads to collisions

# Hash functions:
# Perfect hash function: maps each item to a unique slot
# Goal: create a hash functions that minimizes # of collisions, is easy to compute, and evenly distributes items in the hash table

# folding method: for hash functions, divides items into equal-sized pieces and calculating a hash based on a manipulation of those pieces (e.g., divide a phone number into two-digit numbers and add them together, then take the remainder)

# mid-square method: square the item, then extract some portion of the remaining digits

# can create based on strings - can take the ordinal value of characters

def hash_function(a_string, table_size):
	"""Calculates a hash of a string given a table size."""

	string_sum = reduce(lambda a, x: a + ord(x), list(a_string), 0)
	return string_sum % table_size

print hash_function('hello', 100)

# collision resolution
# when two items hash to the same slot, there must be a systematic method for placing the second item in the hash table

# open addressing: tries to find the next open slot
# linear probing: systematically visiting each slot one at a time
# disadvantage: clustering

# general name for finding another open slot: rehashing

# quadratic probing: skipping quadratically (1, 3, 5, 7, 9, etc.)

# chaining - can hold a reference to a collection/chain of items