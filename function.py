# def function_name(arguments):       #function creation
#                   #function body
#                   return
# function_name()   #function calling


# def display():
#     print("amal")
# display()


# def my_fun(name) :
#     print(name)
# my_fun("apple")
# my_fun("orange")
# my_fun("grapes")


# def add(a,b) :
#     sum = a+b
#     return sum
# x = add(20,30)
# print(x)


#Required arguments:(if 2 arguments created,that 2 have to be passed
# def display(a,b) :
#     print(a,b)
# display(20,30)


#keyword arguments :(can assign values)
# def display(a,b) :
#     print(a,b)
# display(b=20,a=10)

##default arguments:
# def display(a,b=20):
#     print(a,b)
# display(10,30)
# display(10)


##variable length arguments:
# def softronics(*courses):  ## * used for adding more elements
#     for i in courses :
#         print(i)
# softronics('python','java','html')


# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ("apple","banana","cherry")
# my_function(fruits)


##creating empty function using "pass"
# def empty():
#     pass


# def word() :
#     string = "python functions tutorial"
#     x = 5
#     def number() :
#         print(string)
#         print(x)
#     number()
# word()



##recursive:
##function calling itself :
# def fact(n) :
#     if (n == 0 or n == 1) :
#         return 1
#     else :
#         return n*fact(n-1)
# n = int(input("enter the num:"))
# result = fact(n)
# print(result)



# name = "amal"
# def display():
#     age = 25
#     print(name)
#     print(age)
# display()
#
# def display1():
#     print(name)
# display1()



##a lambda function in python is a small anonymous function
# x = lambda a : a + 10
# print(x(5))
#
# y = lambda b,c : b+c
# print(y(5,12))



# def find_max(a,b) :
#     if a > b :
#         return a
#     else :
#         return b
# num1 = int(input("enter num1:"))
# num2 = int(input("enter num2:"))
# result = find_max(num1,num2)
# print("the maximum number:",result)



# def add(a,b) :
#     return a+b
# def sub(a,b) :
#     return a-b
# def mult(a,b) :
#     return a*b
# def div(a,b) :
#     return a/b
# print("1.addition\n2.subtraction\n3.multiplication\n4.division")
# x = int(input("select the option:"))
# num1 = int(input("enter num1:"))
# num2 = int(input("enter num2:"))
# if x == 1 :
#     result = add(num1,num2)
# if x == 2 :
#     result = sub(num1,num2)
# if x == 3 :
#     result = mult(num1,num2)
# if x == 4 :
#     result = div(num1,num2)
# print(result)





list = []

def add_book() :
    id = input("Enter ID:")
    book = input("Enter the book name:")
    price = input("enter the price:")
    author = input("author name:")
    publisher = input("publisher:")
    l1 = []
    l1.append(id)
    l1.append(book)
    l1.append(price)
    l1.append(author)
    l1.append(publisher)
    list.append(l1)
    print(list)
def display_book() :
    id = input('Enter the id for diplaying book:')
    for i in list:
        if i[0] == id:
            print(i)

def update_book() :
    id = input('Enter the id for updating book:')
    for j in list :
        if j[0] == id :
            print("1.book\n2.price\n3.author\n4.publisher")
            y = int(input("select the option for updating"))
            if y == 1 :
                j[1] = input("new book name:")
                print(j)
            if y == 2 :
                j[2] = input("new price:")
                print(j)
            if y == 3 :
                j[3] = input("new author:")
                print(j)
            if y == 4 :
                j[4] = input("new publisher:")
                print(j)
def delete_book() :
    id = input('Enter the id for deleting book:')
    for k in list :
        if k[0] == id :
            list.remove(k)
            print(list)
while True :
    print("1.adding book\n2.displaying book\n3.updating book\n4.deleting book\n5.Break")
    x = int(input("select the option:"))
    if x == 1 :
        add_book()
    if x == 2 :
       display_book()
    if x == 3 :
        update_book()
    if x == 4 :
        delete_book()
    if x == 5 :
        break
























