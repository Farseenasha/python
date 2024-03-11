list =[]
def add_book():
    id = input("enter your ID:")
    book = input("enter book name:")
    price = input("enter price:")
    author = input("author:")
    publisher = input("publisher:")

    l1 = []
    l1.append(id)
    l1.append(book)
    l1.append(price)
    l1.append(author)
    l1.append(publisher)
    list.append(l1)
    print(list)

