import numpy

def prime_finder():
    
    """
    This function calculates the value of the 10001st prime number.
    """
    #We know from the problem's statment that prime_list starts with the values included in our prime_list
    prime_list =[2, 3, 5, 7, 11, 13]
    
    #The next potential value for prime would be 13+2 = 15 (A prime can not be even number except #2)
    pot_prime = 15
    
    #While prime list length bellow 10.001
    while len(prime_list) < 10001:
        
        #We filter out all numbers that are evenly divisible from any of our prime numbers as it is not a prime
        if 0 in pot_prime % numpy.array(prime_list):
            
            #skeeping even numbers will increase our efficienty by almost 50%
            pot_prime += 2
        
        else:
            
            prime_list.append(pot_prime)
            pot_prime += 2
     
    return prime_list[10000]
        
