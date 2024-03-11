#Python dictionary is an ordered collection.It stores elements in key:value pairs.
#Can identify values using key.

#EMPTY DICTIONARY:
# dict = {}
# print(dict)

##adding elements by input in dictionary
# dic = {}
# key = int(input("enter the key:"))
# value = input("enter the value:")
# dic[key] = value
# print(dic)



###MAIN PRGRM USED IN THIS FILE:###
dict = {1:"blue" , 2:"black" , 3:"white"}
print(dict)

#finding value using key:'[]' or '.get()' :
print(dict[2])
print(dict.get(2))

#printing only "keys" alone:
x = dict.keys()
print(x)
#printing only values alone :
y = dict.values()
print(y)

#updating or giving new value for the key :
# dict[1] = "red"
# print(dict)
      ###OR##Another METHOD
# dict.update({1:"red"})
# print(dict)

##Deleting any elements using 'key': ""pop"" or ""popitem""
# dict.pop(1)
# print(dict)
       ### OR ###
# dict.popitem()  ## popitem is used to remove last element:
# print(dict)

#for clear the dictionary:
# dict.clear()
# print(dict)





