# initialize

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')




# Function
def how_many(aDict):
    '''
    this function counts how many items are in the value

    input: aDict - dictionary

    outputs the number of the item
    '''
    count = 0
    values = aDict.values()
    for item in values:
        count += len(item)
    return count

#printing the value
print(how_many(animals))