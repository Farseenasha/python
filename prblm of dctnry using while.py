# dic = {}
# while True:
#     print("1.Create\n2.Display\n3.Update\n4.Delete\n5.break")
#     x = int(input("Select the option:"))
#
#     if x == 5 :
#         break
#
#     if x == 1 :
#         a = int(input("Enter number for creation:"))
#         for i in range(a):
#
#            key = int(input("Enter the key"))
#            value = input("enter the value")
#            dic[key] = value
#         print(dic)
#
#     if x == 2 :
#         b = int(input("Enter the key"))
#         if b in dic :
#             print(dic[b])
#
#     if x == 3 :
#         c = int(input("Enter the key for update"))
#         if c in dic :
#             dic[c] = input("enter new value")
#             print(dic)
#
#     if x == 4 :
#         d = int(input("Enter the key for delete"))
#         if d in dic :
#             dic.pop(d)
#             print(dic)




##SAME AS ABOVE PRBLM:
dic = {}
while True :
    print("1.Create\n2.Display\n3.Update\n4.Delete\n5.break")
    x = int(input("Select the option:"))

    if x >= 5 :
        break

    if x == 1 :
        a = int(input("Number of creation:"))
        for i in range(a) :
            key = int(input("Enter the key:"))
            value = input("Enter the value:")
            dic[key] = value
            print(dic)

    if x == 2 :
        a = int(input("Enter the key for display:"))
        if a in dic :
            print(dic[a])

    if x == 3 :
        a = int(input('Enter the key for update the value:'))
        if a in dic :
            dic[a] = input('Enter new value')
            print(dic)

    if x == 4 :
        a = int(input('Enter key for delete'))
        if a in dic :
            dic.pop(a)
            print(dic)












