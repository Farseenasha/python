##EXPECTATION HANDLING :
#An expectation handling can be defined as an abnormal condition in a program resulting
# in the disruption in the flow of the program.
#Whenever an exception occures, the programe halts(stops) the execution , and
# thus the further code is not executed.

# python provides us with the way to handle the Exception so that the other part of the code can be
#executed without any disruption.



##SYNTAX error:
# if 10 > 1  ## here colon is not used .its an error
#     print("10 is largest")

##LOGICAL ERROR :
# a = 10
# b = 5
# c = a- b ##here the result exception is 15.but due to symbol of "-" we will get it as 5
# print(c)

##RUNTIME ERROR :(here when it write the code,we can'nt understand the error.but when it runs
#3the error is displayed
# a = 10
# b = 0
# c = a/b
# print(c)

##HANDLiNG EXCEPTION ERRORS USING try AND except
# try :
#     x = int(input("enter num1:"))
#     y = int(input("enter num2:"))
#     z = x/y
#     print(z)
# except ValueError :
#     print("value or format error") ##here other than numbers like symbols or characters
# except ZeroDivisionError :
#     print("can't divide by zero")


# try :
#     l1 = [2,4,5,7,3]
#     print(l1[12])
# except IndexError :
#     print("index out of range")


# try :
#     f = open("simple.txt",'r')
#     print(f.read())
# except FileNotFoundError :
#     print("file not found")

# try :
#     from a1 import display
#     a1.display()
# except ModuleNotFoundError :
#     print("module not found")


# try :
#     dict = {1:"say" , 2:"hi" , 3:"hello"}
#     print(dict[5])
# except KeyError :
#     print("key not found")

##format of exception handling
# try :
#     run this code
# except :
#     run this code when exception occures
# else :
#     run this code if no exception occure
# finally :
#     always run this code


try :
    a = 20
    b = 30
    c = a/b
    print(c)
except:
    print("exception occured")
else :
    print("no exception")
finally :
    print("program ends")




