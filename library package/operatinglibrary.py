from addbook import add_book
from displaybook import display
from updatebook import update_book
from deletebook import delete_book
while True :
    print("1.add book\n2.display book\n3.update book\n4.delete book\n5.quite")
    x = int(input("select option:"))
    if x == 1 :
        add_book()
    if x == 2 :
        display()
    if x == 3 :
        update_book()
    if x == 4 :
        delete_book()
    if x == 5 :
        break
