# Recursion

# def factorial(n):
#     # number shouldn't be Negative
#     # num == 0 or num==1 returns 1
#     # n*fact(n-1)

#     if n<0:
#         return 'Number should not be Negative'
    
#     if(n==0 or n==1):
#         return 1
    
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
# num = 5
# fact = factorial(num)
# print(fact)

# Recursion

# def fact(n):
#     if n<0:
#         return '-ve Numbers not Allowed'
    
#     if n==0 or n == 1:
#         return 1
    
#     else:
#         return n*fact(n-1)
    
# userInput = int(input("Enter the Number"))

# factNum = fact(userInput)
# print(f"Factorial is {factNum}")

# using BuiltIn Modules
# import math
# num = 5
# print(f"the Factorial of Number {num} is {math.factorial(num)}")
# num1 = 30
# num2 = 50
# print(f"The GCD of {num1} and {num2} is {math.gcd(num1,num2)}")


# def is_Palindrome(string):

#     cleaned = string.replace(" ","").lower()

#     return cleaned == cleaned[::-1]

# userInput = input("Enter a String: ")

# if is_Palindrome(userInput):
#     print("Palindrome")

# else:
#     print("Not a Palindrome")


# Ask how many elements
# n = int(input("How many elements? "))

# numbers = []
# for i in range(n):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# print("Your list:", numbers)
