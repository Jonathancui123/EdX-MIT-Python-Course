#Apply a function to a list of values
"""def ApplyToEach (L, f):
    new = []
    for i in range(len(L)):
        new.append(f(L[i]))
    return new

L = [1, -2, 3.4]

print(ApplyToEach(L, round))
print(ApplyToEach(L, abs))"""

#Apply a list of functions to a value
"""L = [abs, round, ]

def applyFuncs (funcs, x):
    for func in funcs:
        print(func(x))

applyFuncs(L, -3.4)"""

#Map generalization
L = [1, -2, 3, -4]
new = []
for elt in map(abs, L):
    new.append(elt)
print(new)



