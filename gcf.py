def oddOrEven(x):
    if x % 2 == 1:
        print('Odd')
    else:
        print('Even')

def factors(x):
    factorsList = []
    for i in range (x):
        if x % (i + 1) == 0:
            factorsList.append(i + 1)
    print(factorsList)

factors(15)