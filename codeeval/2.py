def isPalindrome(num):
	"""Input: Any integer
	   Output: Boolean for whether the number is a palindrome"""
	# convert to string for indexing
	num = str(num)
	# base case - it's one or 0 numbers and inherently palindromic
	if len(num) == 1:
		return True
	# otherwise, if the first and last letters are the same, recurse
	else:
		if num[0] == num [-1]:
			# if it's the last two numbers, you're done
			if num[1:-1] == '':
				return True
			# otherwise, check if the middle is palindromic
			else:
				if isPalindrome(num[1:-1]):
					return True
		else:
			return False

def isPrime(num):
	"""Input: Any integer
	   Output: Boolean for whether the number is prime"""

	if num % 2 == 0:
		return False

	for i in range(3, num/2 + 1):
		if num % i == 0:
			return False

	else:
		return True

def largestPrimePalindrome(max):
	"""Input: A maximum number under which to look for a prime palindrome
	   Output: The largest prime palindrome less than the max"""

	# you're not going to get an even prime, so skip every other number
	# also start at the end - you only need the first one from the end
	if max % 2 == 0:
		for i in range(max - 1, 1, -2):
			# much quicker to check if palindrome, so do that first
			if isPalindrome(i):
				if isPrime(i):
					return i
	else:
		for i in range(max - 2, 1, -2):
			if isPalindrome(i):
				if isPrime(i):
					return i

print largestPrimePalindrome(1000)