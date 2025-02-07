""" def login(password):
    #if statement evaluates to true, go to next line.
    if password == 'secret':
        print('logged in')
    else:
        print('incorrect')
x = input('what da password')
login(x) """

""" def grade(score):
    if score >=92:
        print("A")
    elif score >=82:
        print('B')
    elif score >=72:
        print('C')
    else:
        print('F')
x = int(input('what da score '))
grade(x) """ 

""" def gamble(age, id):
    if age >= 21:
        if id:
            print('Gamble away')
        else:
            print('You need ID verification')
    else:
        print("You're too young")
 """
""" def gamble(age, id):
    if age >= 21 and id == True:
        print('have fun')
    elif age >= 21 and id == False:
        print('You need ID verification')
    else:
        print("You're too young") """

raining = True

if not raining == True:
    print('go for walk')
if raining == False:
    print('go for walk')
