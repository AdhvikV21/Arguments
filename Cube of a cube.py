#Define function to calculate cube
def cube (number):
    return number*number*number

#Define a function that will execute cube function if the user entered number is divisble by 3
def by_cube(number):
    if number %3 == 0:
        return cube(number)
    else: 
        return False
#Display result
print(by_cube(9))
print(by_cube(4))