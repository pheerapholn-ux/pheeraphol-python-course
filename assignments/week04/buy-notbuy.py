# โปรแกรมช่วยตัดสินใจเลือกซื้อสินค้าภายใต้งบประมาณรวม

print("Enter prices of 6 items:")
items = []
for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    items.append(price)

print() 

budget = int(input("Enter total budget: "))
print() 

current_total = 0
bought_items = []

for i in range(len(items)):
    price = items[i]

    if current_total + price <= budget:
        print(f"Item {i+1} = {price} -> buy")
        current_total += price
        bought_items.append(price)
    else:
        print(f"Item {i+1} = {price} -> cannot buy")
    
    print(f"Current total = {current_total}")
    print() 

print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {budget - current_total}") 