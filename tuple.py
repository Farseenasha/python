#Empty tuple
tuple = ()
print(tuple)

#type
t1 = (1,3,6,7,9,3)
print(type(t1))

#nested tuple
t2 = ("mouse", [8, 4, 6], (1, 2, 3))
print(t2)

#index 0 1 2  3   4  5
t3 =  (9,7,8,"s","f",8)
print(t3.index("s"))
#       in 1st position its index value
print(t3[1])
print(t3[-2])#negative indexing

#count
print(t3.count(8))

#slicing
t4 = (34,"r","gun",56,"y")
print(t4[1:4])
print(t4[0:5])
print(t4[:-1])

#repetetion
print(t4*2)


