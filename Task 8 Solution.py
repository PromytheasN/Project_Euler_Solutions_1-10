import math

#Importing our number as a string
str1 = ('73167176531330624919225119674426574742355349194934'\
        '96983520312774506326239578318016984801869478851843'\
        '85861560789112949495459501737958331952853208805511'\
        '12540698747158523863050715693290963295227443043557'\
        '66896648950445244523161731856403098711121722383113'\
        '62229893423380308135336276614282806444486645238749'\
        '30358907296290491560440772390713810515859307960866'\
        '70172427121883998797908792274921901699720888093776'\
        '65727333001053367881220235421809751254540594752243'\
        '52584907711670556013604839586446706324415722155397'\
        '53697817977846174064955149290862569321978468622482'\
        '83972241375657056057490261407972968652414535100474'\
        '82166370484403199890008895243450658541227588666881'\
        '16427171479924442928230863465674813919123162824586'\
        '17866458359124566529476545682848912883142607690042'\
        '24219022671055626321111109370544217506941658960408'\
        '07198403850962455444362981230987879927244284909188'\
        '84580156166097919133875499200524063689912560717606'\
        '05886116467109405077541002256983155200055935729725'\
        '71636269561882670428252483600823257530420752963450')
    
def max_digits_product(str1):
    
    """
    This function returns the greatest product of the 13 adjacent digits in any string of numbers or 
    integars that we may input.
    """
    

    i = 0
    adj_digits = []
    
    #Assigning a value to the variable that will store our largest product
    product = 0
    
    #Making a list of integers from our string using list comprehension 
    int_list = [int(x) for x in list(str1)]
    
    #Creating a loop to check all the potential compinations of 13 adjacent digit numbers within our list
    while i < len(str1)-12:
        
        i +=1
        
        #Filtering out smaller than our current product, products
        if math.prod(int_list[i:i+13]) > product:
            
            product = math.prod(int_list[i:i+13])
            
            #This is the list of numbers that gave our largest product atm
            adj_digits = int_list[i:i+13]
            
    print(adj_digits)
    return product
