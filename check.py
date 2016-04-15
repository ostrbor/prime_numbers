#Function is used in two files.

def is_prime(num):
    '''
    If 'a*b=c' then either 'a' or 'b' is '<=sqrt(c)' and
    another multipier is '>=sqrt(c)'. So no need to go through 
    whole range(2,num).
    '''
    for i in range(2, int(num**0.5)):
        if num % i == 0: return False
    return True
