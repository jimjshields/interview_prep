import unittest

class TestFib(unittest.TestCase):

	def setUp(self):
		self.input = 5
		self.output = 8
		self.input_2 = 11
		self.output_2 = 144

	def test_fib(self):
		self.assertEqual(fib(self.input), self.output)
		self.assertEqual(fib(self.input_2), self.output_2)

def fib(n):
	"""Returns the nth number in the fibonacci sequence, w/ 1st index at 0."""

	if n in (0, 1):
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


class TestMaxNum(unittest.TestCase):

	def setUp(self):
		self.input = [1, 2, 3, 4, 5]
		self.output = 5
		self.input_2 = [-100, -1, -2]
		self.output_2 = -1

	def test_max_num(self):
		self.assertEqual(max_num(self.input), self.output)
		self.assertEqual(max_num(self.input_2), self.output_2)

def max_num(num_list, largest_so_far=None):
	"""Returns the maximum number in a list of ints."""

	if num_list == []:
		return largest_so_far
	if num_list[0] > largest_so_far:
		largest_so_far = num_list[0]
	return max_num(num_list[1:], largest_so_far)


class TestListSum(unittest.TestCase):

	def setUp(self):
		self.input = [1, 2, 3, 4, 5]
		self.output = 15
		self.input_2 = [-100, -1, -2]
		self.output_2 = -103

	def test_list_sum(self):
		self.assertEqual(list_sum(self.input), self.output)
		self.assertEqual(list_sum(self.input_2), self.output_2)

def list_sum(num_list, total=0):
	"""Returns the sum of a list of ints."""

	if num_list == []:
		return total
	else:
		return num_list[-1] + list_sum(num_list[:-1])


class TestLastIndexOf(unittest.TestCase):

	def setUp(self):
		self.num_1, self.list_1 = 5, [1, 2, 4, 6, 5, 2, 7]
		self.output_1 = 4
		self.num_2, self.list_2 = 5, [1, 2, 4, 6, 2, 7]
		self.output_2 = -1
		self.num_3, self.list_3 = 5, [1, 2, 5, 4, 6, 5, 2, 7]
		self.output_3 = 5

	def test_list_sum(self):
		self.assertEqual(last_index_of(self.num_1, self.list_1), self.output_1)
		self.assertEqual(last_index_of(self.num_2, self.list_2), self.output_2)
		self.assertEqual(last_index_of(self.num_3, self.list_3), self.output_3)

def last_index_of(num, num_list, last_index=-1, current_index=0):
	"""Returns the last index of num in num_list; -1 if not in num_list."""

	if current_index >= len(num_list):
		return last_index
	else:
		if num_list[current_index] == num:
			last_index = current_index
		current_index += 1
		return last_index_of(num, num_list, last_index, current_index)


if __name__ == '__main__':
	unittest.main()