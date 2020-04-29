def lg_prime_factor(nm):
    div = 2
    prime_factorlist = []
    
    #We check with this loop if the number can still be divided
    #and that is not prime by checking if the dividers multiplied are smaller
    #than it
    while div * div <= nm:
        
        #we test if current divider gives us a clean division
        #if not, then we increase the divider until we get a clean division
        if nm % div != 0:
            div = div + 1
        
        #if number can be clearly divided by divider then
        #we can reduce the number to the next dividend
        #as it is not prime
        else:
            nm = nm // div
            
            #we add the divider to the list of prime factors
            prime_factorlist.append(div)
    
    #if div * div > of the number it means that number is prime (except if 1)
    #as 1 does not count in primes
    if nm > 1:
        #we add our number in our prime list
        prime_factorlist.append(nm)
        
        #we return the largest prime number from our list
    return max(prime_factorlist)
