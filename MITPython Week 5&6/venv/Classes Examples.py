#EXAMPLE ONE! Creating a "fractions" class

class fraction (object):
    #Rational representation of a fraction i.e. not a float!

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    #print representation
    def __str__(self):
        return (str(self.numer) + " / " + (str(self.denom)))
    #adding fractions
    def __add__(self, other):
        newNumer = self.numer * other.denom + other.numer * self.denom
        newDenom = self.denom * other.denom
        return fraction(newNumer,newDenom)

    #subtracting fractions
    def __sub__(self, other):
        newNumer = self.numer * other.denom - other.numer * self.denom
        newDenom = self.denom * other.denom
        return fraction(newNumer,newDenom)

    #SIMPLIFY
    def simplify(self):
        for commonGuess in range (min(self.denom, self.numer), 0, -1):
            if (self.denom % commonGuess == 0) and (self.numer % commonGuess == 0):
                simpleNumer = int(self.numer / commonGuess)
                simpleDenom = int(self.denom / commonGuess)
                break
        return fraction(simpleNumer, simpleDenom)

    #converting fraction to float
    def __float__(self):
        newFloat = self.numer / self.denom
        return newFloat

#Testing my class!
fourEigths = fraction(4,8)
print(fourEigths)

fourFourteenths = fraction(4,14)
print(fourFourteenths)

sum = fourEigths + fourFourteenths

print(sum, "simplified is", sum.simplify())
print(sum.simplify(), "as a float is", sum.__float__())
