# converting an integer to a string in any base

# first convert to base 10 string

def convertToStringBase10(num):
	convString = "0123456789"
	if num < 10:
		return convString[num]
	else:
		first_nums = num / 10
		last_num = num % 10
		return convertToStringBase10(first_nums) + convertToStringBase10(last_num)

print convertToStringBase10(23442554453435)

def toStr(num, base):
	convString = "0123456789ABCDEF"
	if num < base:
		return convString[num]
	else:
		first_nums = num // base
		last_num = num % base
		return toStr(first_nums, base) + convString[last_num]

print toStr(10, 2)

# reverse a string recursively
def reverse(s):
	if len(s) == 1:
		return s
	else:
		return s[len(s) - 1] + reverse(s[:len(s)-1])

# print reverse('hello')

def isPalindrome(s, length):
	if len(s) == 1:
		return s
	else:
		reverseStr = s[-1] + isPalindrome(s[:-1], len(s))
		if len(s) != length:
			return reverseStr
		else:
			if s == reverseStr:
				return True
			else:
				return False

print isPalindrome('racecar', 7)
