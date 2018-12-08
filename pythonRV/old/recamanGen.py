
def recaman(height): 
    numGen = []
    curPlace = 0
    givenHeight = height
    for x in range(0, givenHeight):
        if( not(curPlace-x in numGen) and (curPlace-x > 0)):
            #print(curPlace)
            numGen.append(curPlace-x)
            curPlace -= x
        else:
            #print(curPlace)
            numGen.append(curPlace + x)
            curPlace += x
    print(numGen)
    return numGen

def curAndNext(iterable):
    iterator = iter(iterable)
    current_item = next(iterator)
    for next_item in iterator:
        yield(current_item, next_item)
        current_item = next_item
    yield(current_item, None)
    
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step