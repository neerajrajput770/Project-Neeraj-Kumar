# print("Hello wolrd ")
# if 5>2:
#     print("5 is greater than 2")

# x=5
# y=3
# print(x+y)
# print(x*y)
# print(x/y)
# print(x-y)

# print("this is python")

# x=13
# y="neeraj"
# print(x)
# print(y)

# x=4.5
# print(type(x))

# x=4
# y=5
# print(bool(x+y))
# print(bool(x))


# x=""
# print(bool(x))
# x="5"
# print(bool(x))


# my_var=40
# print(my_var)


# x,y,z="30", "40", "50"
# x="30", "40" , "50"
# print(x )

# fruits=["apple", "banana", "cherry"]
# x,y,z=fruits
# x=y=z=fruits
# print(type(x))

# fruits=[2,4,7,4,6,8,9,10]
# print(fruits)
# print(type(fruits))

# x="python"
# y="is"
# z="good"
# print(x,y,z)
# print(x+y+z)

# #x=good

# def my_func():
#     print("python is "+ x)
#     my_func()  

# my_list=["apple", "banana", 1, 3, 5, 7]

# my_list[2:5]=["abc"]

# print(my_list)
 


# text="hello"

# print(text.upper())
# print(text.lower())
# print(text.strip())
# print(text.replace("hello", "world"))
# print(text.split())

# #format string

# x="abc"
# y=15
# print(f"my name is {x} and my age is {y}") 


# #assigment operators

# x=10
# x-=3   # aise hi sab karnna hai (+,_,*,**,/,)
# print(x)



# #comparsion operators

# x=5
# y=10
# print(x==y)
# print(x!=y)
# print(x>=y)
# print(x<=y)
# print(x<y) 


# #logical operators

# x=10
# print(x>3 and x<11)
# print(not(x>3))

# #ldentity operators

# x=[1,2,3]

# y=x
# z=[1,2,3]
# print(x is y)


# # python sets 

# colors={"red", "green", "blue"} #creating sets 
# print(colors) 
# colors.add("yellow") #adding elements
# print(colors)
# colors.remove("green") #removing elements
# for color in colors: #lterating through set 
#     print(color)


#     #python dictionaries
# students={"name": "abc", "age":18, "grade": "a"}
# print(students)
# print(students["name"])
# print(students.get("age"))


# #if...else in python 

# age=20 
# if age>=18:
#     print("you are adult")
# else:
#     print("you are not adult")    





# list1=[1,2,3,4,5,6]

# list1.insert(2,"apple")
# print(list1)

# list1.append("banana")
# print(list1)

# list1.remove("apple")
# print(list1)

# list1.pop()
# print(list1) 

# list1.clear()
# print(list1)

# list1=[]

# list1.append(1)
# print(list1)

# list1[0]="hello"
# print(list1)

# #loopslists

# list1=[1,2,3,4,4,4,5,]
# for x in list1:
#     print(x)  


# #the if..elif..else statement

# age=20 

# if age>=18:
#     print("you are adult")

# elif age==18:
#     print("you are teen")

# elif age==17:
#     print("you are 17")   

# elif age==16:
#     print("you are 16") 

# else: 
#     print("you are not adult")



# x=15
# if x>10:
#     print("x is greater than 10 ")

#     if x>20:
#         print("x is greater than 20 ")
#     else:
#         print("x is not greater than  

# x=15

# if x%2==0:
#     print("even")

# else: 
#     print("odd")   

# word="python"

# for x in word:
#     print(x)


# for i in range(9):
#     print(i)

# for i in range(1,10,2):
#     print(i)


# for i in range(1,4):
#     for j in range(1,3):
#         print(f"i={i},j={j}")
    
# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)
    

#print all numbers form 1 to 20 using a ffor loop 

# for i in range(1,21):
#     print(i)

# print all even numbers less than 30 using range()

# for i in range(2,31,2):
#     print(i)

# lterate over a list of your favotite colors annd print each one 

# colors = ["red", "blue", ]
# for color in colors:
#     print(color)

#python  functions 

# def greet():
#     print("heelo, python!")
# greet()



# def greet(name):
#     print(f"hello , {name}")

# greet("alice")    
# greet("bob")

#function with parameters
#parameters allow us to pass values into a function when we call it.

# def function_name(parameter1, parameter2):
#     #code block

# def greet(name):
#     print(f"Hello, {name}!")
# greet("Alice")
# greet("Bob")

#function with return value
# return statement allows a function to send back a value to the caller.


#function with addition
# def add(a, b):
#     return a + b

# result = add(5, 3)
# print("Sum:", result)  #output: Sum: 8
# # Function with multiple parameters
# def multiply(x, y):
#     return x * y
# print("Multiplication:", multiply(4, 5))  #output: Multiplication: 20
# #function with subtraction
# def subtract(x, y):
#     return x - y
# print("subtraction:", subtract(10, 4))  #output: subtraction: 6
# #Function with division
# def divide(x, y):
#         return x / y
# print("division:", divide(20, 4))  #output: division: 5.0



# # # Function with default parameters
# # #you can give default values to a parameter.
# def greet(name="Student"):
#     print(f"Hello, {name}!")
# greet()          #uses default value ("Student")  output: Hello, Student!
# greet("Alice")  #overrides default value   output: Hello, Alice!


#scope of variables
#scope refers to the visibility and lifetime of a variable within a program.
# global variable
# global variable is defined outside of any function and can be accessed from anywhere in the code.

# x=10  #global variable
# def my_function():
#     y = 5  #local variable
#     print("Value of y inside function:", y)  #accessing local variable
#     print("Value of x inside function:", x)  #accessing global variable
#     print(x, y)  #output: 10 5
# my_function()  #output: Value of x inside function: 10
# print("Value of x outside function:", x)  #output: Value of x outside function: 10


# local variable
# local variable is defined within a function and can only be accessed within that function.





# # Q.1 Write a function greet() that prints "Hello!".
# def greet(): 

#     print("Hello!")
# greet()  #output: Hello!

# # Q.2 Write a function that adds two numbers and returns the result.
# def add_numbers(a, b):
#     return a + b
# result = add_numbers(5, 3)
# print("Sum:", result)  #output: Sum: 8

# # Q.3 Write a function with a default parameter that prints "Hello, <name>!".
# def greet(name="Student"):
#     print(f"Hello, {name}!")
# greet()          #uses default value ("Student")  output: Hello, Student!
# greet("Alice")  #overrides default value   output: Hello, Alice!


# # Q.4 Write a function that accepts multiple numbers using *args and returns their sum.
# def sum_numbers(*args):
#     return sum(args)
# result = sum_numbers(1, 2, 3, 4, 5)
# print("Sum of numbers:", result)  #output: Sum of numbers: 15


# # Q.5 Write a function that accepts keyword arguments like name, age, grade and prints them.
# def print_student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_student_info(name="Alice", age=18, grade="A")
# #output:
# # name: Alice
# # age: 18
# # grade: A


# # Q.6 Create a lambda function to find the square of a number.
# square = lambda x: x ** 2
# print("Square of 5:", square(5))  #output: Square of 5: 25

# # Q.7 Write a function that demonstrates local and global variable.
# x = 10  # global variable
# def demonstrate_scope():
#     y = 5  # local variable
#     print("Value of y inside function:", y)  # accessing local variable
#     print("Value of x inside function:", x)  # accessing global variable
# demonstrate_scope()  # output: Value of y inside function: 5
# print("Value of x outside function:", x)  # output: Value of x outside function: 10












#OOPs in python
# OOPs stands for Object - Oriented Programming system --> Organizing code using classes and objects.

# Provides a clear structure for the program.
# Makes code easier to maintain,reuse and debug.

# for opening emojis click on window + . (dot) or window + ; (semicolon)

# Class: A blueprint for creating objects. It defines attributes and methods.
# Object: An instance of a class. It contains data and can perform actions defined by the


# class.

# class Car:
#     def _init_(self, brand,color):
#         self.brand = brand    # attribute
#         self.color = color    # attribute

    # method
    # def drive(self):
    #     print(f"Car: {self.brand} {self.color} is driving 🚗.")

 # Objects
# car1 = Car("BMW", "Red")  # creating an object of the Car class
# car2 = Car("Defender", "Blue")  # creating another object of the Car class

# car1.drive()  # calling the drive method on car1
# car2.drive()  # calling the drive method on car2
# # Output:
# Car: BMW Red is driving 🚗.
# Car: Defender Blue is driving 🚗.



#pyhtoon arrays 

# import array

# number=array.array('i',[1,2,3,4,5])
# print(number)


#python -m piip install numpy

# from numpy import random

# x=random.randint(10000)
# print(x)

# x=random.rand()
# print(x)


# [68]
# [1,2,3,4,5]

# [[[1,2,3],
#  [4,5,6]]
# [[7,8,9],
#  [10,11,12]]]
 
# x=random.randint(100,size=(3,5))
# print(x)

# x=random.randint(100,size=(2,2,3,5))
# print(x)


# x=random.choice([3,5,7,9],size=(1))
# print(x)

#pandas

import pandas as pandas

# data=[10,20,30,40,50]
# s=pandas.Series(data)

# print(s)



# data=[["Neeraj"],["Abhishek"],["Raam"],["Manjeet"],["Dheeraj"],["Shyam"]]
# s=pandas.Series(data)

# print(s) 

# data={
#      "Name":["Neeraj", "manjeet","dheeraj","abhi"],
#     "Age":[18,19,17,20],
#     "City":["delhi","bihar","up","uk"]
# }
    

# df=pandas.DataFrame(data)

# print(df)



# data={
#     "Name":["Kunal","Raj","Anish","Rohit","Mohit"],
#     "Age":[17,18,19,18,20],
#     "city":["Bihar","UP","Hariyana","MP","CG"]
# }

# df=pandas.DataFrame(data)

# print(df)

# print(type(df))


import numpy as np

arr=np.array([1,2,3,4,5])
s=pandas.Series(arr) 
print(s)


data={"math":90,"Science":80,"Eenglish":85,}
s=pandas.Series(data)
print(s)   



import pandas as pd 
df = pandas.read_csv("crocks.csv") # file copy karni hai 
print(df.head())

