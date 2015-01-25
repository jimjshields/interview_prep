# running up a staircase w/ n steps
# can hop 1, 2, or 3 steps at a time
# write a function that, given the length of the staircase, 
# gives you the number of ways to go up the stairs

# can be at most n/3 3s, n/2 2s, and n 1s

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

def stairs(n, steps=[], stepsList=[]):
	if len(stepsList) == factorial(n):
		return stepsList
	if sum(steps) == n:
		stepsList.append(steps)
		steps = []
		stairs(n)
	else:

