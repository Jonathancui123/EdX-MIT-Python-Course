def checkPrime(num):
    for divisor in range(2, int(num**0.5)+1):
        if num % divisor == 0:
            return False
    return True

#Three version of a primes iterator
#First, using a primes iterator class

class Primes:
    def __init__(self, rangeMax):
        self.max = rangeMax
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number > self.max:
            raise StopIteration
        elif checkPrime(self.number):
            return self.number
        else:
            return self.__next__()

#Secondly, using a generator:
def genPrimes(num, max):
    """Takes two integers, and returns iterator of all prime numbers between the two numbers inclusive"""
    for x in range(num, max + 1):
        if checkPrime(x):
            yield x

#Variation: Generator for unlimited primes, can be implemented using a for loop to find the first n primes
def unlimPrimes():
    num = 1
    while True:
        num += 1
        if checkPrime(num):
            yield num


max = 50
#Thirdly, using a generator expression:\
primesGenObj = (i for i in range (2, max) if checkPrime(i))
#Demonstrate what an equivalent LIST would look like:
primesList = [i for i in range(2, max) if checkPrime(i)]

