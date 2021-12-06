a, b, c = "Python", "Django", "MySQL"

print(a)
print(b)
print(c)


# # a = b = c = "Fullstack Developer"
# print(a)
# print(b)
# print(c)


# a = "Python-Django"
# b = "Fullstack Developer"
# print( a + b )


# #convert from integer type to float:
# a = float(3)

# #convert from float type to integer:
# b = int(4.5)

# #convert from integer type to complex:
# c = complex(3)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))


# import random

# print(random.randrange(5, 10))


# a_int = 456
# b_flo = 4.56

# c = a_int + b_flo

# print("datatype of a_int:",type(a_int))
# print("datatype of b_flo:",type(b_flo))

# print("Value of c :",c)
# print("datatype of c:",type(c))


# number_int = 123
# number_str = "456"

# print("Data type of number_int:",type(number_int))
# print("Data type of number_str before Type Casting:",type(number_str))

# number_str = int(number_str)
# print("Data type of number_str after Type Casting:",type(number_str))

# number_sum = number_int + number_str

# print("Sum of number_int and number_str:",number_sum)
# print("Data type of the sum:",type(number_sum))


# a="pythonx"

# print ( len (a))

# a = "Mashup, Stack!"

# b = a.split(",")

# print ( b )


# a = " hello how are you"

# b = "how" in a

# print(b)


a = "dogs"
print("I love {0}".format(a))


print("I love {b}".format(b="cats"))


a = "cats"
b = 9
print("I love %s and %d" % (a, b))


age = 50
test = "Walter is {} years old."
print(test.format(age))


language = "Python"
framework = "Django"
version_django = 2
stack = " {} is a programming language. Framework is {} ,and its version is  {:.1f} ."
print(stack.format(language, framework, version_django))


print(1 < 2)
print(1 == 2)
print(1 > 2)

print("________________N_E_X_T_____________________")

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("________________N_E_X_T_____________________")


x = 10
y = 5
# Add two operands or unary plus
print("x + y =", x + y)
# Subtract right operand from the left or unary minus
print("x - y =", x - y)
# Multiply two operands
print("x * y =", x * y)
# Divide left operand by the right one (always results into float)
print("x / y =", x / y)
# Modulus - remainder of the division of left operand by the right
print("x % y =", x % y)
# Floor division - Quotient when x is divided by y, rounded to the next smallest whole number
print("x // y =", x // y)
# Exponent - left operand raised to the power of right
print("x ** y =", x ** y)

print("________________N_E_X_T_____________________")


a = 1001
b = 1000 + 1

print("a == b", a == b)
print("a is b =", a is b)

print("a is b =", a is not b)

print("________________N_E_X_T_____________________")


a = ["Python", "Django"]
b = ["Python", "Django"]
c = a

print(a is c)
# returns True because c is the same object as a
print(a is b)
# returns False because a is not the same object as b, even if they have the same content
print(a == b)
# to demonstrate the difference between "is" and "==": this comparison returns True because a is equal to y

print("________________N_E_X_T_____________________")
print("________________N_E_X_T_____________________")
print("________________N_E_X_T_____________________")

a = "Welcome to Mashup Stack"
b = {1: "Python", 2: "Django"}

print("W" in a)
print("Mashup" not in a)
print(1 in b)
print("Python" in b)


print(" ___________ L I S T ______________ ")


list_py = ["Python", "Django", 2, ["orange", "apple"]]
print(list_py)

print(list_py[3][1])

print("________________N_E_X_T_____________________")


a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(a[-1])
print(a[-3])
print(a[-2])
print(a[-4])

print(a[2:5])

print(a[-4:-1])


print(a[:5])


odd = [2, 4, 6, 8]
odd[0] = 1
print(odd)
odd[1:4] = [3, 5, 7]
print(odd)


print("________________N_E_X_T_____________________")

course = ["Python", "PHP", "C#", "Javascript", "Java"]
course.clear()
print(course)

print("________________N_E_X_T_____________________")


course_1 = ["HTML", "CSS", "Bootstrap"]
course_2 = ["Python", "Django", "Angular"]
course_3 = course_1 + course_2
print(course_3)


print("________________N_E_X_T_____________________")

course_1 = ["HTML", "CSS", "Bootstrap"]
course_2 = ["Python", "Django", "Angular"]
for x in course_2:
    course_1.append(x)
print(course_1)


print("________________N_E_X_T_____________________")
print("________________N_E_X_T_____________________")


x = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", ["hh", "ii"], "j"]
print(x[0], x[2], x[4])
# x[1] and x[3] are sublists.
print(x[1])
print(x[3])

print("________________TUPLE_____________________")


# Empty tuple
my_tuple = ()
print(my_tuple)
# Tuple having integers
my_tuple = (4, 5, 6)
print(my_tuple)
# tuple with mixed datatypes
my_tuple = (1, "Python", 3.4)
print(my_tuple)
# nested tuple
my_tuple = ("Django", [8, 4, 6], (1, 2, 3))
print(my_tuple)


my_tuple = "hello"
print(type(my_tuple))
my_tuple = ("hello",)
print(type(my_tuple))
my_tuple = ("hello",)
print(type(my_tuple))


my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple
print(a)
print(b)
print(c)


print("-----------------------------------------------------------------------------")


# Accessing tuple elements using indexing
my_tuple = ("p", "e", "r", "m", "i", "t")

print(my_tuple[0])  # 'p'
print(my_tuple[5])  # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])  # 's'
print(n_tuple[1][1])  # 4


print("- - - - - - - - - - - -- - - - - - - - - - - - -- - - - - - - - - - - - - ")


# # Deleting tuples
# my_tuple = ('M','A','S','H','U','P','S','T','A','C','K')
# # can't delete items
# # TypeError: 'tuple' object doesn't support item deletion
# # del my_tuple[3]
# # Can delete an entire tuple
# del my_tuple
# # NameError: name 'my_tuple' is not defined
# print(my_tuple)


thistuple = ("banana", "apple", "orange")

for x in thistuple:
    print(x)

course = ("python", "css", "django", "php")
if "python" in course:
    print('Yes "python" is Present')

print(len(course))

print(course.count("python"))
print(course.index("php"))


# joining two tuples

newtuple = thistuple + course

print(newtuple)


my_set = {1, 2, 3}
print(my_set)
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)


# initialize a with {}
a = {}
print(type(a))
# initialize a with set()
a = set()
print(type(a))


course = {"python", "php", "css"}
for x in course:
    print(x)
course.add("javascript")
course.update(["laravel"])
print(course)


print(len(course))

course.remove("php")

print(len(course))


course = {"Python", "PHP", "Java"}
x = course.pop()
print(x)
print(course)


course = {"Python", "PHP", "Java"}
course.clear()
print(course)


course = {"Python", "PHP", "Java"}
# del course
print(course)


set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3}
set_3 = set_1.union(set_2)
print(set_3)


print(
    "---------------------------------------------------------------------------------"
)


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use | operator
print(A | B)


print(A.union(B))
# Output : {1, 2, 3, 4, 5, 6, 7, 8}
print(B.union(A))
# Output : {1, 2, 3, 4, 5, 6, 7, 8}


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use & operator
print(A & B)


print(A.intersection(B))
# Output : {4, 5}

print(B.intersection(A))
# Output : {4, 5}


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use - operator on A
print(A - B)


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)


# dictonary


course = {"language": "Python", "framework": "Django", "version": 2.0}
print(course)


course = dict([("language", "Python"), ("framework", "Django"), ("version", 2.0)])
print(course)
print(course["language"])
print(course.get("framework"))


course["framework"] = "flask"
print(course)

course["year"] = 1995

print(course)


course.pop("year")

print(course)


course.popitem()
print(course)


course = {"language": "Python", "framework": "Django", "version": 2.0}
#  for x in course:
#    print(x)


# for x in course:
#     print(course[x])

# for x in course.values():
#     print(x)


course = {"language": "Python", "framework": "Django", "version": 2.0}
for x, y in course.items():
    print(x, y)

if "language" in course:
    print("Yes, 'language' is one of the keys in this course dictionary.")


course = {"language": "Python", "framework": "Django", "version": 2.0}
mycourse = course.copy()
print(mycourse)


squares = {x: x * x for x in range(6)}
print(squares)


# functions..

print("---------------------FUNCTIONS-----------")


def hello(name):
    print("hi i am", name)


hello("kiron")


def add(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first


result = add(1, 2, 3, action="sum", number="first")
print("Result: %d" % (result))


def course(course_list):
    for x in course_list:
        print(x)


course_list = ["Python", "PHP", "Java"]
course(course_list)


def cube(num):
    return num * num * num


print(cube(3))


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


num = 100
print("The factorial of", num, "is", factorial(num))


class MyClass:
    x = 10


obj1 = MyClass()

print(obj1.x)


print("--------------------------------------------------------")


class Course:
    def __init__(self, language, framework):
        self.x = language
        self.y = framework


obj1 = Course("Python", "Django")

print(obj1.x)
print(obj1.y)


print("------------------------------------------  -----------------------------")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hello my name is " + self.name)


stud1 = Student("Kevin", 26)
stud1.intro()

stud2 = Student("Ron", 25)
stud2.intro()


# x= int (input( "Enter a Number between 0 and 2 : "));


# def lansel(*language):
#     print("You have selected" + language[x])


# language = ["C","Python","PHP"]

# if x <= 2:
#     lansel(x);
# else:
#     print(" Invalid entry")


print("===================================================================")


from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length ** 2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())


from abc import ABC, abstractmethod


class Polygon(ABC):

    # abstract method
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("Triangle have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("Pentagon have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("Hexagon have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("Quadrilateral have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()


class employee:
    def __init__(self):
        self.name = "Kevin"
        self.salary = 10000

    def __str__(self):
        return "name=" + self.name + " salary=$" + str(self.salary)


e1 = employee()
print(e1)


print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


class distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __add__(self, x):
        temp = distance()
        temp.ft = self.ft + x.ft
        temp.inch = self.inch + x.inch
        if temp.inch >= 12:
            temp.ft += 1
            temp.inch -= 12
            return temp

    def __str__(self):
        return "ft:" + str(self.ft) + " in: " + str(self.inch)


d1 = distance(3, 10)
d2 = distance(4, 4)

print(d1 + d2)

import modulefile

print(modulefile.greeting("India"))


import modulefile as m

print(m.greeting("kerala"))

from modulefile import *

print(greeting(" Palakkad "))

print(hai(" raj"))


# id's value may be different in your case.

a = 2
print("id(2) =", id(2))

print("id(a) =", id(a))

print("--------------------------------------------------------")

a = 2
print("id(a) =", id(a))

a = a + 1
print("id(a) =", id(a))

print("id(3) =", id(3))

b = 2
print("id(b) =", id(b))
print("id(2) =", id(2))

print("------------------------------")
print("------------------------------")
print("------------------------------")

a = 5
print("id(a) =", id(a))
a = "Hello World!"

print("id(a) =", id(a))

a = [1, 2, 3]
print("id(a) =", id(a))

print("------------------------------")
print("------------------------------")
print("------------------------------")


import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)
x = datetime.date.today()
print(x)


from datetime import datetime

current = datetime.now()  # current date and time

year = current.strftime("%Y")
print("year:", year)

month = current.strftime("%m")
print("month:", month)

day = current.strftime("%d")
print("day:", day)

time = current.strftime("%H:%M:%S")
print("time:", time)

date_time = current.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)

timestamp = 1591014926
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)

d = date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d = date_time.strftime("%I%p")
print("Output 5:", d)


import json

with open("D:\Documents\Mashupstacks\labs\Python\class.json") as s:
    data = json.load(s)
print(data)


# student_dict = {"name": "Kevin",
# "languages": ["Python", "Java"],
# "married": False,
# "age": 26
# }

# with open('student.txt', 'w') as json_file:
#   json.dump(student_dict, json_file)

# This willcreate a student.txt file


import re

text = "Kevin is 26 years old. He was born on 21st May 1994."
pattern = "\d+"
result = re.findall(pattern, text)
print(result)
result2 = re.split(pattern, text)
print(result2)


text = "Mas\
hup\n Stack"
# RegEx for matching whitespace character
pattern = "\s+"
# before replacing
print(text)

# empty string
replace = ""
new_text = re.sub(pattern, replace, text)
print(new_text)


print("-----------------=============---------------")


# import module sys to get the type of exception
import sys

randomList = ["a", 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)


# program to print the reciprocal of even numbers

# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)


# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)
# finally:
#     print("This is always executed.")


# a = "Good Morning"

# if not type(a) is int:
#   raise TypeError("Only integers are allowed")


#   f= open ("student.txt")


f = open("test.txt", "r")
print(f.read())

print(f.read(6))


f = open("test.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())


f = open("test.txt", "r")
for x in f:
    print(x)


f = open("test.txt", "a")
f.write("We have added more contents to the file.")
f.close()
f = open("test.txt", "r")
print(f.read())


print("------------------------------------")

import csv

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for x in reader:
        print(x)

print("------------------------------------")

import csv

with open(
    "people.csv",
    "r",
) as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        print(row)

print("------------------------------------")
import csv

with open("protagonist.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])


import csv

csv_rowlist = [
    ["SN", "Movie", "Protagonist"],
    [1, "Lord of the Rings", "Frodo Baggins"],
    [2, "Harry Potter", "Harry Potter"],
]
with open("protagonist.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)


print("+++++++++++++++++++++++++++++++++++++++")


def reverse(s):
    a = ""
    for i in s:
        a = i + a
    return a


s = "Python is clean."

print("The original string  is : ", s)
print("The reversed string(using loops) is : ", reverse(s))

print("+++++++++++++++++++++++++++++++++++++++")


def reverse(string):
    string = "".join(reversed(string))
    return string


s = "Python is powerful."

print("The original string  is : ", s)
print("The reversed string(using reversed) is : ", reverse(s))


print("==============================================================")


import random

print("Printing random number using random.random()")
print(random.random())
print("Random integer is", random.randint(0, 9))


import random

city_list = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]
print("Random element from list:", random.choice(city_list))


import math

r = 3
circumference = 2 * math.pi * r
print(
    "Circumference of a Circle = 2 * {0} * {1} = {2}".format(math.pi, r, circumference)
)


import math

print(math.exp(0))


import math

print(math.pow(2, 4))


print(math.sqrt(100))
print(math.sqrt(5))
print(math.ceil(6.78))
print(math.floor(6.78))
print(math.ceil(6.25))
print(math.floor(6.25))


import statistics

data = [1, 3, 5, 7, 9]
print("Harmonic Mean is % s " % (statistics.harmonic_mean(data)))


original = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(original))

result = []
for x in original:
    if x not in result:
        result.append(x)

print("The list after removing duplicates : " + str(result))


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


print(operate(dec, 3))

print("--------------- ------------------- ----------------------- ------------------")

import os

print(os.name)

print(os.getcwd())

print(os.listdir())


def cube(x):
    return x * x * x


num = (1, 2, 3, 4)
output = map(cube, num)
print(output)

# converting map object to list
cube_numbers = list(output)
print(cube_numbers)


# importing functools for reduce function
import functools

# importing operator for operator functions
import operator

# initializing list
numbers = [
    2,
    4,
    6,
    8,
    10,
]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, numbers))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, numbers))

# using reduce to concatenate string
print("The concatenated string is : ", end="")
print(functools.reduce(operator.add, ["Python", "is", "Awesome."]))


import sys

print(sys.version)


i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


def test_fuct(x, y):
    print(x + " " + y)


test_fuct("python", "is awesome")
