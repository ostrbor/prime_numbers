#!/usr/bin/env python

#Factorization of product into two prime numbers.

from check import is_prime

product = input('Enter public key: ')
primes = []

for i in range(3, int(product**0.5)+1):
    if is_prime(i): primes.append(i)

for i in primes:
    if product % i == 0 and is_prime(product//i):
        print(i, product/i)
        break
