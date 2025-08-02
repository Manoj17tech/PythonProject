# re-usable blocks of code, 
# to perform the specific task again and again.

# syntax : 
# parameter : like a variable which holds the value to get used in the function
# def funtionName(parameter):
    # code to be executed

# function Calling using fnName()

# def greet(name,msg):
#     print(f"Hello {name}, {msg}")

# greet("Shakthi","How are you")
# greet("Manoj","Had ur meal ?")
# greet("Manu")

# def addition(a,b):
#     return a+b

# result = addition(10)
# print(result)

# def calcAge(currentYear, birthYear):
#     return currentYear - birthYear

# userInput = int( input("Enter your BirthYear"))
# userAge = calcAge(2025,userInput)
# print(f"Your Age is {userAge}")


# Defualt Parameter (Arguments) :

# def greet(name='Manoj',age=25):
#     print(f'Name is {name} and age is {age}')

# greet()
# greet('shakthi',10)
# greet(10,'Shakthi')
# greet('shakthi')


# *args
# 10,20,30,40
# def addNumbers(*args):
#     total = 0

#     for num in args:
#          total += num

#     print(total)

# addNumbers(10,20,30,50,60,70,90,100,200,500)

# def OrderTakeAway(d1,d2,d3):

#     print(f"Your Orders are {d1}, {d2} , {d3}")

# dish1 =  input("Enter Dish 1")
# dish2 =  input("Enter Dish 2")
# dish3 =  input("Enter Dish 3")

# OrderTakeAway(dish1,dish2,dish3)



# Lambda : one liner functions, which we used to write the samaller functions
# Anonymous Function
# defined with lambda Keyword

# add = lambda x,y :x+y

# sum = add(10,20)
# print(sum)


# map () : 

numbers = [1,2,3,4,5,6,7,8,9,10]

# squares = list(map(lambda x:  x*x, numbers))

# print(squares)

# print(sqauredNumbers)

# evenNumbers = list(filter(lambda x:x%2 ==1,numbers))

# print(evenNumbers)

























