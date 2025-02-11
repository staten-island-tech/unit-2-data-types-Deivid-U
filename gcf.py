""" def oddOrEven(x):
    if x % 2 == 1:
        print('Odd')
    else:
        print('Even')

number = input('Enter a number:')

oddOrEven(number)
 """
""" def factors(x):
    factorsList = []
    for i in range (x):
        if x % (i + 1) == 0:
            factorsList.append(i + 1)
    print(factorsList)

number = input('Enter a number: ')

factors(int(number)) """

def gcf(x, y):
    commonFactorsList = []
    for i in range (x):
        if x % (i + 1) == 0 and y % (i + 1) == 0:
            commonFactorsList.append(i + 1)
    print(max(commonFactorsList))

x = int(input('Enter a number: '))
y = int(input('Enter a number: '))

gcf(x,y)