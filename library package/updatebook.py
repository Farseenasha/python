from addbook import list
def update_book():
    id = input("enter your id for updating the book:")
    for i in list :
        if id == i[0] :
            print("1.book name\n2.price\n3.author\n4.publisher")
            x = int(input("select your option:"))
            if x == 1 :
                i[1] = input("new book name:")
                print("id:",i[0])
                print("book name:",i[1])
                print("price",i[2])
                print("author",i[3])
                print("publisher:",i[4])
            if x == 2 :
                i[2] = input("new price:")
                print("id:", i[0])
                print("book name:", i[1])
                print("price", i[2])
                print("author", i[3])
                print("publisher:", i[4])
            if x == 3 :
                i[3] = input("new author:")
                print("id:", i[0])
                print("book name:", i[1])
                print("price", i[2])
                print("author", i[3])
                print("publisher:", i[4])
            if x== 4 :
                i[4] = input("new publisher:")
                print("id:", i[0])
                print("book name:", i[1])
                print("price", i[2])
                print("author", i[3])
                print("publisher:", i[4])
