import sympy

"""
Thoughts:
1) Create a prime list
2) Sum the prime list
"""

def prime_list(num):
    """
    This function generates prime list list up to the range = num
    """
    #Creating a prime list using sympy.primerange function
    prime_list = list(sympy.primerange(0, num + 1))
    return prime_list                

#We print the sum of the prime list generated up to 2 million.
print(sum(prime_list(2000000)))    
