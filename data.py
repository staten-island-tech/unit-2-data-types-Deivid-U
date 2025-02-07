""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15] """
""" print(values) """
""" for i in values:
    print(i) """

""" print(values[0])
print(values[6])
print(values[7]) """

""" x = "this is a thing" """
""" y= x.split( )
z = y[0]
print(y)
print(z) """

""" x = input("Sentence: ")
words = len(x.split( ))
print("Word count:" + str( words)) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" #if we run this code, the if temp > 68 conditional will fail, then the elif temp == 68 will fail, and then finally the else will run and print the string 'cold'
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

def oddOrEven(x):
    if x % 2 == 1:
        print('Odd')
    else:
        print('Even')

oddOrEven(41)
