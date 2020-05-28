import numpy


def small_divident():
    """
    This is a function that calculates the smallest divident number,
    evenly divisable by all numbers between 1 to 20.
    """
    
    #If our number is evenly divisable with the list bellow, it should be evenly divisable with
    #1 to 10 as well as all the numbers bellow are primes or multiples of numbers of 1 to 10.
    #This will increasae the time efficiency of our function.
    #Here we create an array of our list using NumPy module
    div_array = numpy.array([20,19,18,17,16,15,14,13,12,11])
    
    #20*19 = 390, that would be the smallest possible number that could be divided both from 20 and 19.
    #Using that number instead of just adding 20 for each failed attempt will increase time efficiency 
    num = 390
    nofound = True
    
    while nofound:
        
        #Checking if we have evenly division between num and our array
        div = num % div_array
        
        #Checking if all elements in our div list are 0
        if all(element == 0 for element in list(div)):
            nofound = False
            
        #If not we increase num and repeat the process
        else:
            num += 390
    return num
