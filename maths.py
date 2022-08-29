def sum(a,b):
    '''This adds the two numbers'''
    print(a+b)
    
def subtract(a,b):
    '''This subtracts the two numbers'''
    print(a-b)
    
def pallindrome(a):
    '''Gives whether the string is a pallindrome or not'''
    if str(a)[::-1]==str(a):
        print('The string is a pallindrome')
    else:
        print('The string is not a pallindrome')
        
def even_odd(a):
    '''Gives whether a number is even or odd'''
    if a%2==0:
        print('The number is even')
    else:
        print('The number is odd')
        
def is_prime(a):
    '''Gives whether a number is prime or not'''
    for n in a:
        if a%n==0:
            print('The number is prime')
            break
    else:
        print('The number is not prime')