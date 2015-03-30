# -*- coding:utf-8 -*-

# Threads defined by a class

import time
import threading

# Inherit from Thread
class CountdownThread(threading.Thread):
	def __init__(self, count):
		# Initialize the thread
		threading.Thread.__init__(self)
		self.count = count

	# Redefine run — that's the code that'll execute in the thread
	def run(self):
		while self.count > 0:
			print 'Counting down {}'.format(self.count)
			self.count -= 1
			time.sleep(0.2)
		return

# To initialize/call:
a = CountdownThread(10)
b = CountdownThread(20)
# a.start()
# b.start()

def countdown(count):
	while count > 0:
		print 'Counting down: {}'.format(count)
		count -= 1
		time.sleep(0.5)

t1 = threading.Thread(target=countdown, args=(10,))
t1.start()
t2 = threading.Thread(target=countdown, args=(15,))
t2.start()
