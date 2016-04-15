#!/usr/bin/env python

#Find two random prime number of same size
#and return it's product.

from functools import reduce

size = input('Enter size of number: ')
min = 10**(size-1)
max = 10**size-1

def is_prime(num):
    '''
    If a*b=c then either a or b is <=sqrt(c) and
    another is >=sqrt(c). So no need to go through 
    whole range(2,num).
    '''
    for i in range(2, int(num**0.5)):
        if num % i == 0: return False
    return True

def find_primes(min, max):
    '''Find two different biggest prime number'''
    res = []
    for i in range(max, min, -1):
        if is_prime(i): res.append(i)
        if len(res) == 2: break
    return res

primes = find_primes(min, max)
print(primes)
product = reduce(lambda x,y: x*y, primes)
print(product)
