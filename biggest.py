# initialize
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

#function
def biggist(aDict):
    '''
    aDict: a Dictionary, where all values are list
    returns: The key with the largest number of values associated with it
    '''
    biggest_key = str()
    biggest_value = 0
    key = aDict.keys()
    for k in key:
        if int(len(aDict[k])) >= biggest_value:
            biggest_value = int(len(aDict[k]))
            biggest_key = k
    return biggest_key


print(biggist(animals))