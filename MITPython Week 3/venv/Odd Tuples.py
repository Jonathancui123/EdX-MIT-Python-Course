def OddTuples(aTup):
    count = 0
    NewTup = ()
    while count < len(aTup):
        NewTup = NewTup + (aTup[count],)
        count += 2
    return NewTup

def OddTuples2 (aTup):
    return  aTup[::2]

aTup = ('I', 'am', 'a', 'test', 'tuple')

print(OddTuples2(aTup))