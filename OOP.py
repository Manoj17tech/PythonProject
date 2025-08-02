# OOP'S: programming Paradigm

# Object : instance of a Class
# class : Blueprint to Create a Obejct


# by using class Keyword 
# Attributes and Methods

# class Car:
# Creating Car Class
    # def __init__(self,brand,model,seats):
    #     self.brand = brand
    #     self.model = model
    #     self.seats = seats



    # function for the Classes.
    # def showDetails(self):
    #     print(f" {self.brand} Motors has created it's new {self.model} model, it have {self.seats} seats")

# Creating a Car Obejct

# TataCar = Car('TATA','EV',5)

# TataCar.showDetails()

# BMWCar = Car("BMW",'EV',7)
# BMWCar.showDetails()

# print(TataCar.model,TataCar.brand , TataCar.seats)
# print(f"{TataCar.brand} brand released its {TataCar.model} model , having seats of {TataCar.seats}")

# class House:

#     def __init__(self,floor,bedrooms,no_AC):

#         self.floor = floor
#         self.bedrooms = bedrooms
#         self.no_AC = no_AC

# my_House = House(4,5,6)

# print(my_House.no_AC)

# Inheritance : Parent Inherits the Properties to it's Child Classes.

# Parent Class
# class Animal:

#     def sound():
#         print("Every Animal Makes Sound")

#     def color():
#         print("Every Animal has it's Own Color")


# # Child Class

# class Lion(Animal):

#     def sound():
#         print("Lion Roars")

#     def color():
#         print("Lion color is Orange-brown")

# class Cat(Animal):
#     def sound():
#         print("Cat Meow's")

#     def color():
#         print("Cat color is Black and White")

# kitten = Cat.sound()
# kitten = Cat.color()


# Access specifier : gets the Access to Child Class , properties

# Lion1 = Lion.sound()
# Lion1 = Lion.color()
# print(Lion1)



# pip install reportlab

# from reportlab.lib.pagesizes import LETTER
# from reportlab.pdfgen import canvas

# # Create a new PDF file
# file_path = "sample_output.pdf"
# c = canvas.Canvas(file_path, pagesize=LETTER)

# # Add text to the PDF
# c.drawString(100, 750, "Hello, this is a simple PDF created with Python!")

# # Add another line
# c.drawString(100, 730, "Created using the reportlab library.")

# # Save the PDF
# c.save()


























