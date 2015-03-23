class StackQueue(object):
	"""A queue implemented with two stacks."""

	def __init__(self):
		self.enqueue_stack = []
		self.dequeue_stack = []

	def enqueue(self, item):
		self.enqueue_stack.append(item)

	def dequeue(self):
		if self.dequeue_stack == []:
			while len(self.enqueue_stack) > 0:
				self.dequeue_stack.append(self.enqueue_stack.pop())
		return self.dequeue_stack.pop()

q = StackQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print q.enqueue_stack
print q.dequeue_stack
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()