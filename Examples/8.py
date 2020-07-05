"""
8. Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""
from pyparsing import range


def is_prime(num):
    if num > 3:
        for i in range(4, num):
            if num % i == 0:
                return False
            else:
                return True
    elif num >= 0:
        return True
    else:
        raise ValueError('Please enter a valid integer')


print(is_prime(num=0))
