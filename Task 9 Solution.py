#from operator import mul
from functools import reduce
"""
Planing of our steps for solution.
1) Make a list with lists with all the potential combination of numbers that can be equal with 1000 while a<b<c
2) Filter the list and keep the list that a**2 + b**2 = c ** 2 
3) Calculate product of values of our list
"""




def list_checker(triplet_list):
    """
    This function filters if for 3 numbers of a list a,b,c a**2 + b**2 = c**2 is True
    """
    
    our_digits =[]

    i = 0
    
    #We may need to repeat this for all our list's values
    while i < len(triplet_list):

        #Filtering out all the lists from our list that are not True to our condition
        #until we find one that is True.
        if triplet_list[i][0]**2 + triplet_list[i][1]**2 == triplet_list[i][2]**2:
            our_digits = triplet_list[i]
        
        i+=1
    return our_digits
    
    
    
    

def list_maker():
    """
    This function creates a list of lists of 3 numbers where a<b<c is true 
    and a+b+c = 1000
    """
    
    #Creating an empty list
    triplet_list = []
    
    #Our list can not be with numbers higher than 999 as a < b < c and a + b + c == 1000
    for a in range(1000):
        
        #Range (a+1, 1000) makes sure that b > a
        for b in range(a + 1, 1000):
            
            #Same here c > b
            for c in range (b + 1, 1000):
                
                #We know already that a < b < c 
                #There for we do not add that condition increase time efficiency by 20 -25%.
                if a + b + c == 1000:
                    triplet_list.append([a,b,c])
    
    return triplet_list

our_digits = list_checker(list_maker())


#We could also do 
#nums_product = reduce(mul, our_digits)

#We are calculating the product of our 3 digit list that honors our conditions
nums_product = reduce( (lambda x, y: x * y), our_digits)
print("The product of the numbers is: ", nums_product)
