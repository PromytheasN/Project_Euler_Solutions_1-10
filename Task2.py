
a, b = 0, 1
fibo_list = [a, b]
while b < 4e6:
    a, b = b, a+b
    fibo_list.append(b)
c = 0
for numb in fibo_list:
    if numb % 2 == 0:
        c = c + numb
print(c)


#Here is an other way to solve this

fib_seq, fib_seq2 = 1, 1 
sum_feb = 0

# Here we make sure that our fib number is bellow 4 million.
while fib_seq <= 4e6:
    
    fib_seq, fib_seq2 = fib_seq2, fib_seq + fib_seq2 
    
    #Here we make sure that we add only even values to our SUM
    
    if fib_seq % 2 == 0:
        sum_feb = sum_feb + fib_seq
print(sum_feb)
