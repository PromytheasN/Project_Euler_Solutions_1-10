def dif_of_squares():
    """
    This function returns the difference of the squares between 
    the squared result of the addition of the first 100 numbers
    and the addition of the squares of the first 100 numbers.
    """
    
    #Calculating the sum of the squares of 1 to 100 and store the value on num1
    num1 = sum([x**2 for x in range(101)])
    
    #Calculating the square of the sum of 1 to 100 and store the value on num2
    num2 = sum(list(range(101)))**2
    
    #It could also be a one liner: return sum(list(range(101)))**2 - sum([x**2 for x in range(101)])
    return num2 - num1
