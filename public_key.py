#!/usr/bin/env python

#Find two random prime number of same size
#and return it's product.

from functools import reduce
from check import is_prime

size = input('Enter size of number: ')
min = 10**(size-1)
max = 10**size-1

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
