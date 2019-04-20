def checkPrime(num):
    for divisor in range(2, int(num**0.5)+1):
        if num % divisor == 0:
            return False
    return True

#Three version of a primes iterator
#First, using a primes iterator class

class Primes:
    