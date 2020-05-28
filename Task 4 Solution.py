def largest_pal_number():
    
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    polylist, polylist2 = [],[]
    
    #Creating a list with all the 5 digit polymer numbers
    for polymer in range(10000,99999):
    
        #Filter out all non-polymer numbers
        if str(polymer)[:2] == str(polymer)[:2:-1]:
            polylist.append(polymer)
    
    #Creating a list with all the 6 digit polymer numbers
    for polymer2 in range(100000, 999999):
    
        #Filter out all non-polymer numbers
        if str(polymer2)[:3] == str(polymer2)[:2:-1]:
            polylist2.append(polymer2)
    
    #Combine our polymere lists
    poly = polylist + polylist2
    
    #Reverse our polymere list in order to start from the largest possible number
    #This will increase the efficiency of our function later on
    poly.reverse()

    #In this loop we start from the largest polymer number in our list and start dividing it 
    #with 3 digit dividers until we find a QUOTIENT that is integar
    #The first Quotient that is integer will point the first there for largest polymer
    #number of our list that fulfills our criteria. 
    for polymer_num in poly:
        for divident in reversed(range(100,1000)):
            if polymer_num % divident == 0 and 99 < polymer_num//divident < 1000:
                return polymer_num
