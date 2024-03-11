list = []
print(list)

l1 = ["hat", "mat" , "rat" , 13, 15]
print(l1)

l1.append('sat')
print(l1)

l1.insert(3,'sat')
print(l1)

l1[2] = 'cat'
print(l1)

l1.remove('cat')
print(l1)

#pop used to remove the list: pop alone will remove last of the list
l1.pop()
print(l1)

#pop(index position)will remove that index position value
l1.pop(1)
print(l1)

del l1[1]
print(l1)

l1.insert(2,"sat")
print(l1)

print(type(l1))

x = l1.index("sat")
print(x)

l1.insert(4,13)
print(l1)

y = l1.count(13)
print(y)

l2 = ["joe","era",13]
l1.extend(l2)
print(l1)

l3 = [3,5,34,67,23,44,79]
l3.sort()
print(l3)

l4 = [222,456,345,756,384]
print(max(l4))
print(min(l4))

l5 = ['fan','man','none','hen','men','gun']
print(l5[1])
print(l5[0:2])
print(l5[2:5])
print(l5[-1])
print(l5[1:4])
print(l5[:6])
print(l5[-1:])

#l5.clear()
#print(l5)