# f = open("file.txt",'r')
# print(f.read())

# with open("file.txt",'r') as f :
#     print(f.read())

#### x is for creating a file:
# f = open("text.txt",'x')
# f.close()

##w can hide the last prgrm &appear new one
# f = open("text.txt",'w')
# # f.write("hello")
# f.write("world")
# f.close()

# f = open("text.txt",'a')
# f.write("welcome")
# f.write("you")
# f.close()

# f = open("file.txt",'r')
# print(f.readline())

###readlines used for getting output as a string
# f = open("file.txt",'r')
# print(f.readlines())

# f = open("file.txt",'r')
# x = f.readlines()
# print(x[0])

# f = open("file.txt",'r')
# print(f.read())

# f = open("file.txt",'r')
# y = f.read()
# for i in y :
#     print(i)

##os is a built in word
# import os
# os.remove("sample")
# print("file removed")

# f = open("text.txt",'r')
# print(f.read())
# # print(f.tell()) ###tell used where the curser is stopped or where the current curser position
# f.seek(1)
# print(f.tell())

##enumerate used to find the word with its index position
# f = open("text.txt",'r')
# x = f.read()
# for i in enumerate(x) :
#     print(i)

f = open("file.txt",'r')
f1 = open("text.txt",'w')
for i in f :
    f1.write(i)






