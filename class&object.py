##python is an object oriented programming language.

##almost everything in python is an object, with its properties(attributes) and methods

##properties(attributes) = variables
##methods = functions

## a class is like an object constructor, or a "blueprint" that defines the structure and behaviour
##of objects

## objects has properties & methods
##instance of class is object

# class student :
#     name = "aisha"  ##attribute ( variables)
# s = student()  ## an object of the class student
# print(s.name)
# d = student()
# print(d.name)
# s.name = "linto"
# print(s.name)
# print(d.name)


# class Student :
#     def display(self,x):
#         print(x)
#     def display2(self):
#         print("peer")
# s = Student()
# s.display("light")
# s.display2()
#
# d = Student()
# d.display("high")
# d.display




# class Calculator :
#     def addition(self):
#         x = int(input("enter a num1:"))
#         y = int(input("enter num2:"))
#         result = (x+y)
#         print("result:",result)
#     def subtraction(self):
#         x = int(input("enter a num1:"))
#         y = int(input("enter num2:"))
#         result = (x-y)
#         print("result:", result)
#     def multiplication(self):
#         x = int(input("enter a num1:"))
#         y = int(input("enter num2:"))
#         result = (x*y)
#         print("result:", result)
#     def division(self):
#         x = int(input("enter a num1:"))
#         y = int(input("enter num2:"))
#         result = (x/y)
#         print("result:", result)
# c = Calculator()
#
# while True :
#     print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.break")
#     a = int(input("select the option:"))
#     if a == 1 :
#         c.addition()
#     if a == 2 :
#         c.subtraction()
#     if a == 3 :
#         c.multiplication()
#     if a == 4 :
#         c.division()
#     if a == 5 :
#         break



###Constructor
##Constructors can be of two types.
## 1. parameterized Constructor
## 2. non-parametarized Constructor

## All classes have a function called __init__(),which is always executed when the class is being initiated.
## The __init__() function is called automatically every time class is being used to create a new object.
# The constructor is used to initialize the attributes of the object
#In python, the constructor method is named __init__


## Constructor - non parameterized
# A non-parameterized constructor, also known as a default constructor, is a constructor that doesn't
# take any parameters.
#It initializes the attributes of the object eith default values


# class Student:
#     def __init__(self):
#         print("This is non-parameterized constructor")
#     def show(self,name):
#         print("hello",name)
# student = Student()
# student.show("jinu")


##Parameterized constructor
# the parameterized constructor has multiple parameters along with the self.

# class Student:
#     def __init__(self,name):
#         self.name = name ##here self.name is considered as a variable
#     def show(self):
#         print("hello",self.name)
# student= Student("eza")   #object constructing
# student.show()
# student2 = Student("aizi")
# student2.show()


## More than one constructor in single class

# class Student :
#     def __init__(self):
#         print("The first constructor")
#     def __init__(self):
#         print("the second constructor")
# s1 = Student()

## In the above code, the object s1 called the second constructor whereas both have the same
#configuration.
#The 1st method is not accessible by the s1 object. internally, the object of the calss will always
#call the last constructor if the calss has multiple constructor.
#The constructor overloading is not allowed in python.



# class Car :
#     def __init__(self,name,price,color):
#         self.name = name
#         self.price = price
#         self.color = color
#     def start(self):
#         print(self.name +  "started")
# c1 = Car("Duster",800000,"gold")
# c2 = Car("Tata",500000,"silver")
# print(c1.name)
# print(c1.price)
# print(c1.color)
# print(c2.name)
# print(c2.price)
# print(c2.color)
# c1.start()
# c2.start()




# list = []
# class Vehicle :
#     def __init__(self):
#         self.number = 0
#         self.name = 0
#         self.price = 0
#         self.wheel = 0
#     def add(self):
#         self.number = int(input("enter vehicle number:"))
#         self.name = input("vehicle name:")
#         self.price = int(input("price:"))
#         self.wheel = int(input("wheel number:"))
#     def display(self):
#         print("vehicle number:",self.number)
#         print("vehicle name:",self.name)
#         print("price:",self.price)
#         print("wheel number:",self.wheel)
# while True :
#     print("1.add vehicle\n2.display vehicle\n3.break")
#     x = int(input("select the option:"))
#     if x == 1 :
#         v = Vehicle()
#         v.add()
#         list.append(v)
#         print(list)
#     if x == 2 :
#         while True :
#             print("1.two wheeled vehicles\n2.three wheeled vehicles\n3.four wheeled vehicles\n4.break")
#             x = int(input("select the option:"))
#             if x == 1 :
#                 for i in list :
#                     if i.wheel == 2 :
#                         i.display()
#             if x == 2 :
#                 for i in list :
#                     if i.wheel == 3 :
#                         i.display()
#             if x == 3 :
#                 for i in list :
#                     if i.wheel == 4 :
#                         i.display()
#
#             if x == 4 :
#                 break
#     if x == 3 :
#         break





## Destructor
# Python uses a garbage collector to automatically reclaim memory that is no longer in use. However,Python
# does provide a special method called __del__ that is referred to as a "destructor".

# Garbage collection is an essential part of managing memory in dynamic languages(no specification required,
# like c,eg:for number have to specify as integer in c language)like python, where developers don't have
# direct control over memory allocation and deallocation. It helps prevent leaks and contributes
# to the overall robustness of python programs.


# class A:
#     def __init__(self,name):
#         self.name = name
#     def display(self) :
#         print(self.name)
#
#     def __del__(self):
#         print(f"object {self.name} is being destroyed")
# a = A("Reema")
# b = A("Niya")
# a.display()
# b.display()
# del a
# b.display()


# The __str__() function controls what should be returned when the class object is represented as a string.
# class Student :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} ({self.age})"
# s = Student("liya",24)
# print(s)



## Inheritance provides code reusibility to the program because we can use an existing class to create
#  a new class instead of creating it from scratch.

# class Parent:
#     def read(self):
#         print("He can read")
#     def write(self):
#         print("he can write")
# class Son(Parent):
#     pass
# son1 = Son()
# son1.read()
# son1.write()

## Single inheritance
# class A:            #BASE/PARENT class
#     def display(self):
#         print("hello")
# class B(A):         ##derived/child class
#     def display1(self):
#         print("welcome")
# b = B()
# b.display()
# b.display1()

##Multiple inheritance(1 child class & morethan one parent class)

# class A:
#     def display(self):
#         print("hai")
# class B:
#     def display1(self):
#         print("hello")
# class C(A,B):
#     def display2(self):
#         print("welcome")
# c= C()
# c.display()
# c.display1()
# c.display2()



##multilevel inheritance
# class A:
#     def display(self):
#         print("hey")
# class B(A):
#     def display1(self):
#         print("hello")
# class C(B):
#     def display2(self):
#         print("welcome to")
# class D(C):
#     def display3(self):
#         print("ooty")
# d = D()
# d.display()
# d.display1()
# d.display2()
# d.display3()


##Hierarchical inheritance (1 parent class & different child class)
# class A:
#     def display(self):
#         print("hai")
# class B(A):
#     def display1(self):
#         print('HELLO')
# class C(A):
#     def display2(self):
#         print("welcome")
# c = C()
# c.display()
# c.display2()
# b = B()
# b.display()
# b.display1()


##Hybrid inheritance
## Combination of more than one type of inheritance within a single program.
## When a combination of single & multiple inheritance is used in a same program, it is referred as
##  hybrid inheritance.
# class A:
#     def display(self):
#         print("animals")
# class B(A):
#     def display1(self):
#         print("domestic animals")
# class  C(A):
#     def display2(self):
#         print("wild animals")
# class D(B,C):
#     def display3(self):
#         print("dog")
# d = D()
# d.display()
# d.display3()
# d.display1()
# d.display2()
# # c = C()
# # b=B()
# # b.display()
# # b.display1()
# # c.display()
# # c.display2()


# class Student:
#     def __init__(self):
#         self.x = "hello"
# class Teacher(Student):
#     def __init__(self):
#         super().__init__()   #super()__init__() used to avoid clash between the init
#         self.y = "world"     #if this not used it will become error
#     def display(self):
#         print(self.x)
#         print(self.y)
# t = Teacher()
# t.display()



## Polymorphism
## Implementing same thing in different ways.

# class Over:
#     def display(self,a,b):
#         print(a+b)
# c = Over()
# c.display(10,20)
# c.display('hi','welcome')

##Method overloading
## same method different parameters
# class Flash:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
# f = Flash()
# print(f.add(10,20))


## Method overriding
# class Flash:
#     def display(self):
#         print("hlo")
# class Student(Flash):
#     def display(self):
#         print('world')
# s = Student()
# s.display()

# class Father():
#     def home(self):
#         print("kozhikode")
# class Son(Father):
#     def home(self):
#         print("kochi")
# s=Son()
# s.home()



##Abstraction
# It is a process of hiding the implementation details from the user, only highlited set of services
# to the user.
# It allows you to focus on what an object does rather than how it achieves its functionality.


##Encapsulation
# Wrapping up of data
# By using encapsulation we can restrict variables and methods access globally by making it private

# class A:
#     name = "linta"             ###Public
#     def display(self):
#         print("hey,bro")
#         print(self.name)
# obj = A()
# obj.display()
# print(obj.name)


# class A:
#     __name = "Linta"       ###Private(indicated by doublescore)
#     def __display(self):    # Can't access the private methods & attributes outside theclass or
#         print("hi,reem")     # inside another class
#         print(self.__name)
# class B(A):
#     def display1(self):
#         print("ashly")
#         print(self.__name)
# obj = B()                    ##Here class B functions only can access
# obj.display1()
# obj.__display()
# print(obj.__name)
# a = A()
# a.__display()
# print(a.__name)


# class A:
#     _name = "niya"      ##Protected(indicated by single underscore)
#     def _display(self):   # this means,the prgrm we can run it,but actuallywe shouldn't access it nor change the code
#         print("Hello,Linta")
#         print(self._name)
# a = A()
# a._display()
# print(a._name)



# Decorators in python are a powerful and flexible way to modify or extend
# the behaviour of functions or methods without changing their source code.
# Decorators allow you to wrap a function with another function,
# often referred to a "decorator function", which can add functionality,
# modify arguments or return values, or perform other tasks before or after
# the wrapped function is called.

# def my_decorator(func):
#     def wrapper():
#         print("you can see the change")
#         func()
#         print("you can see the change")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("hello")
# say_hello()


# def swapping(func):
#     def inner(a,b):
#         if a<b :
#             a,b = b,a
#         return func(a,b)
#     return inner
# @swapping
# def div(a,b):
#     print(a/b)
# div(4,12)




















































