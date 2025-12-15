#7,8
#Sandwich list oders
sandwich_orders = ['meat','cheese','beef','vergie','tuna']
finished_sandwiches=[]

#Messsage to make each order
while sandwich_orders:
    current_sandwich =sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
finished_sandwiches.append(current_sandwich)

#List of each sandwich made
print("\nSandwiches made:")
for sanwich in finished_sandwiches:
    print(sanwich)

#7,9
#Pastrami appearing in list at list 3 times
sandwich_orders=['pastrami', 'chees', 'pastrami','vergie','tuna','pastrami']
finished_sandwiches=[]
print("Am sorry the deli has run out of pastrami.\n")

#Remove all occurence of pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#Make rest of sandwiches
while sandwich_orders:
    current_sandwich =sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
finished_sandwiches.append(current_sandwich)

#Final list
print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)