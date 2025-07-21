# Laundry Management System using a dictionary

laundry_inventory = {}

def add_item(item_name, quantity, price_per_unit):
    if item_name in laundry_inventory:
        laundry_inventory[item_name]['quantity'] += quantity
        laundry_inventory[item_name]['price_per_unit'] += price_per_unit
    else:
        laundry_inventory[item_name] = {'quantity': quantity, 'price_per_unit': price_per_unit}

def remove_item(item_name, quantity):
    if item_name in laundry_inventory:
        #if quantity >= laundry_inventory[item_name]['quantity']:
        #    del laundry_inventory[item_name]
        if quantity <= laundry_inventory[item_name]['quantity']:
            laundry_inventory[item_name]['quantity'] -= quantity

def calculate_total_cost():
    total_cost = 0
    for item_name, details in laundry_inventory.items():
        total_cost += details['quantity'] * details['price_per_unit']
    return total_cost

# Example Usage:

add_item('T-shirts', 10, 2.50)
add_item('T-shirts', 11, 12.50)
add_item('Jeans', 5, 5.00)

print("Current Inventory:", laundry_inventory)

remove_item('T-shirts', 3)

print("Updated Inventory:", laundry_inventory)

total_cost = calculate_total_cost()
print("Total Cost of Laundry:", total_cost)


"""
dic={}
def add(item_name,qty,pri):
    if item_name in dic:
        dic[item_name]["qty"]+=qty
        dic[item_name]["pri"]+=pri
    else:
        dic[item_name]={"qty":qty,"pri":pri}
def remove(item_name,qty):
    if item_name in dic:
        if qty <= dic[item_name]["qty"]:
            dic[item_name]["qty"] -= qty

add("sga",1,212)
print(dic)
add("DGw",3,45)
add("sga",12,212)
print(dic)
remove("sga",3)
print(dic)
"""
