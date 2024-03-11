# list = []
# while True:
#     print("1:Add book\n2:Display book\n3:Update book\n4:Delete book")
#     x = int(input("Select the option:"))
#     if x >= 5 :
#         print("Invalid Selection!")
#     if x == 1 :
#         id = input("ID:")
#         book = input("Book Name:")
#         price = input("Price:")
#         author = input("Author:")
#         publisher = input("Publisher:")
#         l1 =[]
#         l1.append(id)
#         l1.append(book)
#         l1.append(price)
#         l1.append(author)
#         l1.append(publisher)
#         print(l1)
#         list.append(l1)
#         id2 = input("ID:")
#         book2 = input("Book Name:")
#         price2 = input("Price:")
#         author2 = input("Author:")
#         publisher2 = input("Publisher:")
#         l2 = []
#         l2.append(id2)
#         l2.append(book2)
#         l2.append(price2)
#         l2.append(author2)
#         l2.append(publisher2)
#         print(l2)
#         list.append(l2)
#         print(list)
#
#     if x == 2 :
#         b = input("Select the Book Name:")
#         if b == book :
#             for i in (l1) :
#                 print(i)
#         if b == book2 :
#             for j in l2 :
#                 print(j)
#
#     if x == 3 :
#         b2 = input("Select the Book Name:")
#         if b2 == book :
#             l1[2] = input("New Price of the Book:")
#             print(l1)
#         if b2 == book2 :
#             l2[2] = input("New Price of the Book:")
#             print(l2)
#
#     if x == 4 :
#         b3 = input("Select the Book Name:")
#         if b3 == book :
#             list.pop(0)
#             print(list)
#         if b3 == book2 :
#             list.pop(1)
#             print(list)
#         break






# list = []
# while True:
#     print("1:Add book\n2:Display book\n3:Update book\n4:Delete book")
#     x = int(input("Select the option:"))
#     if x >= 5 :
#         print("Invalid Selection!")
#
#     if x == 1 :
#         id = input("ID:")
#         book = input("Book Name:")
#         price = input("Price:")
#         author = input("Author:")
#         publisher = input("Publisher:")
#         l1 =[]
#         l1.append(id)
#         l1.append(book)
#         l1.append(price)
#         l1.append(author)
#         l1.append(publisher)
#         print(l1)
#         list.append(l1)
#         print(list)
#
#     if x == 2 :
#         id = input("Select the ID:")
#         for i in list :
#             if i[0]==id:
#                 print("ID:",i[0])
#                 print("book:",i[1])
#                 print("price:",i[2])
#                 print("author:",i[3])
#                 print("publisher:",i[4])
#
#     if x == 3 :
#         id = input("Select the ID:")
#         for i in list:
#             if i[0] == id:
#                 i[2] = int(input("Enter new price"))
#                 print("ID:", i[0])
#                 print("book:", i[1])
#                 print("New price:", i[2])
#                 print("author:", i[3])
#                 print("publisher:", i[4])
#
#     if x == 4 :
#         id = input("Select ID:")
#         for i in list:
#             if i[0] == id:
#                 list.remove(i)
#                 print(list)
#             break






# list = []
# while True:
#     print("1.Add book\n2.Display book\n3.Update book\n4.Delete book\n5.break")
#     x = int(input("Select the Option:"))
#     if x >= 5 :
#
#         break
#
#     if x == 1 :
#         id =input("ID:")
#         book = input("Name of the Book:")
#         price = input("Price:")
#         author = input("Author:")
#         publisher = input("Publisher:")
#         l1 = []
#         l1.append(id)
#         l1.append(book)
#         l1.append(price)
#         l1.append(author)
#         l1.append(publisher)
#         list.append(l1)
#         print(list)
#
#     if x == 2 :
#         id = input("Enter ID:")
#         for i in list :
#             if i[0] == id :
#                 print("ID:",i[0])
#                 print("Book:",i[1])
#                 print("Price:",i[2])
#                 print("Author:",i[3])
#                 print("Publisher:",i[4])
#
#     if x == 3 :
#         id = input("Enter ID:")
#         for i in list :
#             if id == i[0]:
#                 while True :
#                     print("Select option for Update")
#                     x = (int(input("1.ID\n2.Book\n3.Price\n4.Author\n5.Publisher\n")))
#                     if x == 1 :
#                         i[0] = input("Update ID:")
#                         print("Updated ID:",i[0])
#                         print("Book:",i[1])
#                         print("Price:",i[2])
#                         print("Author:",i[3])
#                         print("Publisher:",i[4])
#                         break
#                     if x == 2 :
#                         i[1] = input("Update Book Name:")
#                         print("ID:", i[0])
#                         print("Updated Book Name:", i[1])
#                         print("Price:", i[2])
#                         print("Author:", i[3])
#                         print("Publisher:", i[4])
#                         break
#                     if x == 3 :
#                         i[2] = input("Update Price:")
#                         print("ID:", i[0])
#                         print("Book:", i[1])
#                         print("Updated Price:", i[2])
#                         print("Author:", i[3])
#                         print("Publisher:", i[4])
#                         break
#                     if x == 4 :
#                         i[3] = input("Update Author:")
#                         print("ID:", i[0])
#                         print("Book:", i[1])
#                         print("Price:", i[2])
#                         print("Updated Author:", i[3])
#                         print("Publisher:", i[4])
#                         break
#                     if x == 5 :
#                         i[4] = input("Update Publisher")
#                         print("ID:", i[0])
#                         print("Updated Book:", i[1])
#                         print("Price:", i[2])
#                         print("Author:", i[3])
#                         print("Updated Publisher:", i[4])
#                         break
#
#     if x == 4 :
#         for i in list :
#             id = input("Select ID for remove the book details:")
#             if id == i[0] :
#                 list.remove(i)
#                 print(list)
#                 break














