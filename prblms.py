# l1 = [1,2,3]
# l2 = [4,5,6]
# result = []
# for i in range(0,3) :
#     result.append(l1[i] + l2[i])
# print(result)
# ###OR  ANOTHER METHOD:
# c = [l1[0]+l2[0] , l1[1]+l2[1] , l1[2]+l2[2]]
# print(c)


# a = input("enter a word:")
# b = ['a' , 'e' , 'i' , 'o' , 'u']
# count = 0
# for i in a :
#     if i in b :
#         count += 1
# print(count)


# a = 7
# b = 2
# x = a//b ## this is floor division..which means how much times have 2 in 7: which equals 3
# y = a%b ## this is modulus..which means the reminder of 7 divided by 2
# print("a//b=",x)
# print("a%b=",y)
# z =a//b + a%b
# print("a//b + a%b =",z)


# a = "calculator"
# result = ""
# for i in a :
#     if i not in result :
#         result = result + i
# print(result)



# a = [1, 2, 3, 34, 67, 21]
# b = [2, 6, 4, 5, 78]
# c = []
# for i in a:
#     if i not in b :
#         c.append(i)
# print(c)



# a = input("enter a word")
# b = ['a','e','i','o','u']
# count = 0
# for i in a :
#     if i in b :
#         count += 1
# if count <= 3 :
#     print("false")
# if count > 3 :
#     print("true")


####################################
# list = [1, 2, 3, 34, 67, 21]
# a = list.sort()
# x = list[0]
# y = list[-1]
# print(x)
# print(y)


################################
# a = input("enter a word")
# b = " "
# for i in a :
#     if i not in b :
#         b = b + i
# print(b)
# if a in b :
#     print("true")
# if a not in b :
#     print("false")

#######################
##SUM OF ELEMENTS EXCEPT SELF:
# l = []
# l1 = []
# a = int(input("enter the number of elements:"))
# for i in range(a) :
#     n = int(input("enter the values one by one:"))
#     l.append(n)
# print(l)
# sum = 0
# for j in l:
#     sum = sum + j
# print("sum=",sum)
# for k in l :
#     r = sum - k
#     l1.append(r)
# print(l1)


#######################
# A = []
# B = []
# C = []
# def MissingElements() :
#     n = int(input("enter number of elements in A:"))
#     m = int(input("enter number of elements in B:"))
#
#     for i in range(n) :
#         a = int(input("enter the elements of A one by one:"))
#         A.append(a)
#     print("A",A)
#     for j in range(m) :
#         b = int(input("enter the elements of B one by obe:"))
#         B.append(b)
#     print("B",B)
#     for k in A :
#         if k not in B :
#             C.append(k)
#     print(C)
# MissingElements()



############fibonacci
# a = 0
# b = 1
# c = 0
# f = [0,1]
# x = int(input("enter elements for fibonacci:"))
# for i in range(x-2) :
#     c = a + b
#     a = b
#     b = c
#     f.append(c)
# print(f)

##find largest word in a string(xxxxxxx)
# a = input("enter a sentence:")
# splt = a.split()
# max = 0
# # s = len(splt)
# # print(s)
# for i in splt:
#     if len(i)>max:
#         max = len(i)
#         max+=1
#
# print(i)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = 0
# for i in a :
#     if i % 2 == 0 :
#         sum = i + sum
# print(sum)


x = int(input("enter a num1:"))
y = int(input("enter num2:"))
a = x % y






    
















    


























