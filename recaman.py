def searchList(given, find):
    for x in number:
        if(x == find):
            return False
    return True
number = [0]
hstep = input("Highest Step?\n")
currentPlace = 0;
for i in range(1, int(hstep)):
    if(currentPlace - i > 0 and searchList(number, currentPlace-i)):
        number.append(currentPlace - i)
        currentPlace -= i
    else:
        number.append(currentPlace+i)
        currentPlace += i
print(number)

