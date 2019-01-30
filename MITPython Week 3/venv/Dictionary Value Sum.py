animals = { 'a': ['aardvark'], 'b': ['baboon', 'boob', 'belly'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


"""def how_many(aDict):
    count = 0
    for element in aDict.values():
        count += len(element)
    return  count

print(how_many(animals))"""

#Find the longest list in the dictionary
def biggest(aDict):
    lengths = []
    for element in aDict.values():
        lengths.append(len(element))
    k = max(lengths)

    list = []
    for key in aDict:
        if len(aDict[key]) == k:
            list.append(key)

    return list

print(biggest(animals))

