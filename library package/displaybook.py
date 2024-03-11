from addbook import list
def display():
    id = input("enter your id:")
    for i in list:
        if i[0] == id :
            print("book name:",i[1])
            print("price:",i[2])
            print("author:",i[3])
            print("publisher:",i[4])



