l1 = int(input("litre of water used="))
if l1 <= 100 :
    bill = l1*15
elif l1 <= 200 :
    bill = (100*15)+((l1-100)*14)
elif l1 >= 200 :
    bill = (100*15)+(100*14)+((200-l1)*12)
else:
    bill = "invalid"
print(bill)

