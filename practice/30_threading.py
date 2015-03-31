# # -*- coding:utf-8 -*-

# # Threads defined by a class

# import time
# import threading

# # Inherit from Thread
# class CountdownThread(threading.Thread):
# 	def __init__(self, count):
# 		# Initialize the thread
# 		threading.Thread.__init__(self)
# 		self.count = count

# 	# Redefine run — that's the code that'll execute in the thread
# 	def run(self):
# 		while self.count > 0:
# 			print 'Counting down {}'.format(self.count)
# 			self.count -= 1
# 			time.sleep(0.2)
# 		return

# # To initialize/call:
# a = CountdownThread(10)
# b = CountdownThread(20)
# # a.start()
# # b.start()

# def countdown(count):
# 	while count > 0:
# 		print 'Counting down: {}'.format(count)
# 		count -= 1
# 		time.sleep(0.5)

# ### Mutex Lock ###

# def increment():
# 	global x
# 	global x_lock
	
# 	# Suggested pattern for releasing to ensure no control-flow issues.
# 	# Automatically acquires/releases lock when control enters/exits the
# 	# assoc. block of statements.
# 	with x_lock:
# 		for i in xrange(100000): 
# 			x += 1
# 			print 'Thread 1: {}'.format(x)
	
# def decrement():
# 	global x
# 	global x_lock
	
# 	# Suggested pattern for releasing to ensure no control-flow issues.
# 	with x_lock:
# 		for i in xrange(100000):
# 			x -= 1
# 			print 'Thread 2: {}'.format(x)

# x = 0

# # Synchronization Primitives
# # A mutex
# x_lock = threading.Lock()

# # Fixing synchronization issues
# # Without the mutex, there would be threads accessing/changing the shared data 
# # at the same time
# # t1 = threading.Thread(target=increment)
# # t2 = threading.Thread(target=decrement)
# # t1.start(); t2.start()
# # t1.join(); t2.join()
# # With the mutex, this will always be zero
# # print x

# ### RLock ###
# # Lock access to certain methods/functions, rather than data

# class Foo(object):
# 	lock = threading.RLock()
# 	def bar(self):
# 		with Foo.lock:
# 			pass
# 	def spam(self):
# 		with Foo.lock:
# 			self.bar

# ### Semaphore ###
# n = 2
# m = threading.Semaphore(n) # Create a semaphore w/ count of n
# m.acquire() # waits if the count is 0, otherwise decrements count and continues
# m.release() # increments count and signals waiting threads (if any)
# # Unlike locks, acquire()/release() can be called in any order by any thread


# # Resource control
# import urllib
# sema = threading.Semaphore(5) # 5 threads can be executing the function at once
# def fetch_page(url):
# 	sema.acquire()
# 	try:
# 		u = urllib.urlopen(url)
# 		return u.read()
# 	finally:
# 		sema.release()

# ### Events ###

# init = threading.Event()
# def worker():
# 	init.wait() # wait until initialized
# 	# statements...
# 	print 'ready'

# def initialize():
# 	# statements...
# 	print 'Initializing...'
# 	init.set()

# threading.Thread(target=worker).start() # Launch workers
# threading.Thread(target=worker).start()
# threading.Thread(target=worker).start()
# initialize()

# from threading import *

# # Using to signal 'completion'
# # Might use for async processing, etc.

# def master():
# 	item = create_item()
# 	evt = Event()
# 	worker.send((item, evt))
# 	# other processing
# 	# wait for worker
# 	evt.wait()

# def worker():
# 	item, evt = get_work()
# 	evt.set()

# ### Condition Variables ###

# cv = threading.Condition([lock])
# cv.acquire() # acquire underlying lock
# cv.release() # release underlying lock
# cv.wait() # wait for condition
# cv.notify() # signal that a condition holds
# cv.notifyAll() # signal all threads waiting

# # common use: producer/consumer patterns

# items = []
# items_cv = threading.Condition()

# # Producer Thread
# item = produce_item()
# with items_cv:
# 	items.append(item)
# 	items_cv.notify()

# # Consumer Thread
# with items_cv:
# 	while not items:
# 		items_cv.wait()
# 	x = items.pop(0)
# 	# Do something with x

# ### Threads and queues ###

# # Basic queue ops

# from Queue import Queue
# q = Queue(100) # maxsize here: 100
# q.put(item)
# q.get()
# q.empty()
# q.full()

# for item in produce_items():
# 	q.put(item)
# # wait for consumer
# q.join()

# while True:
# 	item = q.get()
# 	consume_item(item)
# 	# Signal that processing is done
# 	q.task_done()

# q.task_done() # signal that work is done
# q.join() # wait for all work to be done

# ### Messages ###

# # pickle

# import pickle

# # serializing an object onto a 'file'
# pickle.dump(someobj, f)

# # unserializing an object from a file
# someobj = pickle.load(f)

# # Can also turn objects into byte strings
# # convert to a string
# s = pickle.dumps(someobj)

# # load from a string
# someobj = pickle.loads(s)


# # an example: launching a subprocess
# import subprocess

# p = subprocess.Popen(['python', 'child.py'], 
# 					stdin=subprocess.PIPE, 
# 					stdout=subprocess.PIPE)

# p.stdin.write(data) # send data to subprocess
# p.stdout.read(size) # read data from subprocess

# # A message channel 

# # channel.py

# import pickle

# class Channel(object):
# 	def __init__(self, out_f, in_f):
# 		self.out_f = out_f
# 		self.in_f = in_f
# 	def send(self, item):
# 		pickle.dump(item, self.out_f)
# 		self.out_f.flush()
# 	def recv(self):
# 		return pickle.load(self.in_f)

# # sample child process
# # child.py
# import channel
# import sys

# ch = channel.Channel(sys.stdout, sys.stdin)
# while True:
# 	item = ch.recv()
# 	ch.send(('child', item))

# # parent process setup
# # parent.py
# import channel
# import subprocess

# p = subprocess.Popen(['python', 'child.py'],
# 					stdin=subprocess.PIPE,
# 					stdout=subprocess.PIPE)
# ch = channel.Channel(p.stdin, p.stdout)

### multiprocessing ###

# import time
# import multiprocessing

# class CountdownProcess(multiprocessing.Process):
# 	def __init__(self, count):
# 		multiprocessing.Process.__init__(self)
# 		self.count = count

# 	def run(self):
# 		while self.count > 0:
# 			print 'Counting down: {}'.format(self.count)
# 			self.count -= 1
# 			time.sleep(0.5)
# 		return

# # Same as w/ threading - inherit from Process and redefine run()
# # Critical detail: always launch in __main__
# # Or can launch w/ target= as w/ threading

# if __name__ == '__main__':
# 	p1 = CountdownProcess(10)
# 	p1.start()

# 	p2 = CountdownProcess(20)
# 	p2.start()

# ### pipes ###

# # returns pair of connection objects
# (c1, c2) = multiprocessing.Pipe()

# c1.send(obj) # send an object
# c2.recv() # receive an object

# c1.send_byes(some_buffer) # send a buffer of bytes
# c2.recv_bytes([max_buffer_size]) # receive a buffer of bytes
# c1.poll([timeout]) # check for data

# Generators/coroutines

def countdown_task(n):
	while n > 0:
		print n
		yield
		n -= 1

from collections import deque
tasks = deque([
	countdown_task(5),
	countdown_task(10),
	countdown_task(15)
])

def scheduler(tasks):
	while tasks:
		task = tasks.popleft()
		try:
			next(task) # run to the next yield
			tasks.append(task) # reschedule
		except StopIteration:
			pass

# run it 
scheduler(tasks)