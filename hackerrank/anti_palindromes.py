def factorial(n):
    fact_dict = {0:0, 1:1}
    for i in xrange(2, n + 1):
        fact_dict[i] = i * fact_dict[i - 1]
    return fact_dict[n]
    
def count_anti_palindromes(n, m):
    """n: number of chars; m: size of alphabet"""
    
    if n % 2 == 0:
        num_palindromes = m ** (n/2)
    else:
        num_palindromes = m ** ((n/2) + 1) 

    num_perms = n ** m
    return num_perms - num_palindromes

print count_anti_palindromes(2, 2)