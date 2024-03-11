# count = 1
# while count <= 5 :
#     print(count)
#     count += 1

# count = 5
# while count >= 0 :
#     print(count)
#     count -= 1


# i = 0
# while i < 5 :
#     i = i+1
#     if i == 3:
#         continue
#     print(i)


# i = 0
# while i < 10:
#     i = i+1
#     if i == 3:
#         break
#     print(i)


#FOR EMPTY FUNCTION:
# while True:
#     pass



# password = input("enter a password:")
# while len(password) <= 8 :
#     print("password must have minimum 8 characters")
#     password = input("re-enter password:")
# print("valid password")



# while True:
#     print("1:Addition\n2:Subtraction\n3:Division\n4:Multiplication\n5:break")
#     x = int(input("select your choice:1,2,3,4,5:"))
#     print(x)
#     if x == 5 :
#         break
#     a = int(input("num 1 ="))
#     b = int(input("num 2 ="))
#     print()
#     if x == 1 :
#         print("result=",a + b)
#         break
#     if x == 2 :
#         print("result=",a - b)
#         break
#     if x == 3 :
#         print("result=",a/b)
#         break
#     if x == 4 :
#         print("result=",a*b)
#         break





while True:
    print("1:square\n2:rectangle\n3:circle")
    x = int(input("select the shape:"))
    print(x)
    if x >=4 :
        print("invalid selection!\nRe-select the shape:")
    if x == 1 :
        a = int(input("a side of the square="))
        print("perimeter of the square=", 4 * a)
    if x == 2 :
        l = int(input("length of the rectangle="))
        w = int(input("width of the rectangle="))
        print("perimeter of the rectangle=",2*(l+w))
    if x == 3 :
        r = int(input("radius of the circle="))
        print("perimeter of the circle=",2*3.14*r)
        break







    


