list = []
while True :
    print("1.Add vehicle\n2.Display vehicle\n3.break")
    x = int(input("Select the option:"))
    if x == 1 :
        no = input("Enter vehicle number:")
        name = input("Enter vehicle name:")
        price = input("Enter price:")
        wheel = int(input("enter the number of wheel:"))
        l1 = []
        l1.append(no)
        l1.append(name)
        l1.append(price)
        l1.append(wheel)
        list.append(l1)
        print(list)
    if x == 2 :
        while True:
            print("wheel of the vehicle:\n1.two wheeled\n2.three wheeled\n3.four wheeled\n4.break")
            y =int(input("select the option:"))
            if y == 1 :
                for i in list:
                    if i[3] == 2 :
                        print(i)

            if y == 2 :
                for i in list:
                    if i[3] == 3 :
                        print(i)

            if y == 3 :
                for i in list:
                    if i[3] == 4 :
                        print(i)
                        
            if y == 4 :
                break

    if x == 3 :
        break





