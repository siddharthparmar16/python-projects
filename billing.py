class Item:
    def __init__(self, id, itemName, price):
        self.id = id
        self.itemName = itemName
        self.price = price

def display(item_list, customer_name, customer_address):
    total = 0
    print("\n\n\n")
    print("\t      D MART    ")
    print("\t   --------------    ")
    print(f"Name : {customer_name} \t Address : {customer_address}\n")
    for obj in item_list:
        print(f"Id : {obj.id} \t ItemName : {obj.itemName}\tPrice : {obj.price}")
        print("------------------------------------------------")
        total += obj.price
    print(f"\t\tTotal : {total}")
    print("\n")
    print("\tThanks for visiting")
    print("\n\n")

item_list = []

print("\n\n")
print("Hello Everyone.......")
customer_name = input("Enter your name       ")
customer_address = input("Enter your address    ")
total_items = int(input("Enter total items    "))
print("\n")


for i in range(0, total_items):
    item_id = (i + 1)
    item_name = input("Enter item name     ")
    item_price = int(input("Enter price    "))
    item_list.append(Item(item_id, item_name, item_price))


display(item_list, customer_name, customer_address)
