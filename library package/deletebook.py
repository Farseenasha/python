from addbook import list
def delete_book():
    id = input("enter id for delete the book:")
    for i in list :
        if i[0] == id :
            list.remove(i)
            print(list)

