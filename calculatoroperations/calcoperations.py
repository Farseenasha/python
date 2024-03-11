from calculator.addition import add
from calculator.subtraction import sub
from calculator.multiplication import mult
from calculator.division import divi



print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.break")
x = int(input("select the option:"))
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
while True :
    if x == 1 :
        result = add(num1,num2)
    if x == 2 :
        result = sub(num1,num2)
    if x == 3 :
        result = mult(num1,num2)
    if x == 4 :
        result = divi(num1,num2)
    if x == 5 :
        break
    print("result=", result)

