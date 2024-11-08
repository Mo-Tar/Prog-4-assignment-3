import random
import requests
from datetime import datetime

##########################################################
# Read functions to work with item.txt anf suppliers.txt #
##########################################################


def read_items_from_json():
    response = requests.get('http://34.29.246.163:8080/api/items')
    
    items = []
    try:
        for entry in response.json():
            items.append({
                'id': entry['ItemID'],
                'name': entry['Name'],
                'quantity': int(entry['Quantity']),
                'price': float(entry['Price']),
                'supplier_id': entry['SupplierID']
            })
    except KeyError as e:
        print(f"Missing key in JSON data: {e}")
    return items


def read_suppliers_from_json():
    response = requests.get('http://34.29.246.163:8080/api/suppliers')
    suppliers = []
    try:
        for entry in response.json():
            suppliers.append({
                'id': entry['SupplierID'],
                'company name': entry['Name'],
                'address': entry['Address'],
                'sales person contact': entry['SalesPersonContact']
            })
    except KeyError as e:
        print(f"Missing key in JSON data: {e}")
    return suppliers


##########################
# Search functions BELOW #
##########################

def search_item(search_value, items):
    for item in items:
        if item['id'] == str(search_value) or item['name'] == str(search_value):
            return item

def search_by_name(search_value, items):
    for item in items:
        if item['name'] == str(search_value):
            return item

def search_by_id(search_value, items):
    for item in items:
        if item['id'] == str(search_value):
            return item
        
########################################
# Functions that Work with Items BELOW #
########################################

def add_item(file_path, id, name, quantity, price, supplier_id, items):
    items.append({
                    'id': id,
                    'name': name,
                    'quantity': int(quantity),
                    'price': float(price),
                    'supplier_id':supplier_id
                })
    update(file_path, items)
    print()
    print("===============")
    print("Adding item...")
    print("Item has been added successfully!")
    print("===============")

def delete_tool(search_value, items, file_path): 
  item_to_delete = search_item(search_value, items)
  if(item_to_delete):
    items.remove(item_to_delete)
    update(file_path, items)
    print()
    print("===============")
    print("deleting item...")
    print("Item has been deleted successfully!")
    print("===============")

  else:
      print(f"No item with the ID or name '{search_value}' was found.")


####################################################
# Functions that keep the item.txt file up to date #
####################################################
        
def remove_content(file_path):
  try:
        with open(file_path, 'r+') as f:
            f.seek(0)
            f.truncate()
            
  except FileNotFoundError:
        print(f"File not found: {file_path}")
        
def update(file_path, items):
  remove_content(file_path)
  try:
      with open(file_path, 'w') as f:
            for item in items:
              new_item = f"{item['id']};{item['name']};{item['quantity']};{item['price']};{item['supplier_id']}\n"
              f.write(new_item)
            # print("file updated successfully.")
  except FileNotFoundError:
        print(f"File not found: {file_path}")
    
##################################################
# Functions that helps create the order.txt file #
##################################################

def check_item_quantity(items):
    less_ten_items = []
    for item in items:
        if item['quantity'] < 10:
            less_ten_items.append(item)
            
    if less_ten_items:
        create_order_list(less_ten_items)
        print()
        print("===============")
        print("Creating orderlist...")
        print("Order list has been created!")
        print("===============")
        return less_ten_items
    else:
        return "There are no items below 10 quantity"

def get_supplier_name(supplier_id):
    suppliers = read_suppliers_from_json()
    for supplier in suppliers:
        if supplier['id'] == supplier_id:
            return supplier['company name']

def create_order_list(low_stock_items):
    date_ordered = datetime.now().strftime("%B %d, %Y") 
    with open('orders.txt', 'a') as file:
        file.write("=" * 60 + "\n")
        for index, item in enumerate(low_stock_items):
            order_id = str(random.randint(0, 99999)).zfill(5)
            amount_ordered = 30 - item['quantity']
            total_cost =  item['price'] * amount_ordered
            supplier_name = get_supplier_name(item['supplier_id'])
            file.write(f"ORDER ID.: {order_id}\n")
            file.write(f"Date Ordered: {date_ordered}\n")
            file.write("\n")
            file.write(f"Item Description: {item['name']}\n")
            file.write(f"Amount ordered: {amount_ordered}\n")
            file.write(f"Supplier: {supplier_name}\n")
            file.write("\n")
            file.write(f"Total cost: ${total_cost}\n")
            
            if index < len(low_stock_items) - 1:
                file.write("-" * 60 + "\n")
        file.write("\n")

##############################
# MENU Functions for display #
##############################

def display_welcome_menu():
    print("===========================")
    print("Welcome to Inventory Menu!")
    print("===========================")

def display_main_menu(items, file_path):
    while True:
        print("")
        print("1. Modify Inventory")
        print("2. Search Inventory")
        print("3. Exit")
        print()
        user_input = input("Please select an option (1-3): ").strip()
        match user_input:
            case "1":
                display_modify_inventory(items, file_path)
                break
            case "2":
                display_search_inventory(items, file_path)
                break
            case "3":
                print("===============")
                print("GoodBye!")
                print("===============")
                break
            case _: 
                print("Invalid please try again")

def display_modify_inventory(items, file_path):
    while True:
        print("")
        print("1. Add tool")
        print("2. Delete tool")
        print("3. Update inventory")
        print("4. Back")
        user_input = input("Please select an option (1-4): ").strip()
        match user_input:
            case "1":
                # user_input_id = validate_item_id(items, "Please input ID of tool: ")
                # user_input_name = input("Please input name of tool: ").strip()
                # user_input_quantity = validate_numerical_input("Please input quantity of tool: ")
                # user_input_price = validate_numerical_input("Please input price of tool: ")
                # user_input_supplier_id = validate_supplier_id("Please input supplier ID: ")
                # add_item(file_path, user_input_id, user_input_name, user_input_quantity, user_input_price, user_input_supplier_id, items)
                print("")
            case "2":
                user_input_search_id = input("Please input the ID or name of the tool: ").strip()
                # delete_tool(user_input_search_id, items, file_path)
            case "3":
                check_item_quantity(items)

            case "4":
                print("")
                main() 
                break
            case _:
                print("Invalid please try again")

def display_search_inventory(items, file_path): 
    while True:
        print("")
        print("1. Search Name")
        print("2. Search ID")
        print("3. Back")
        user_input = input("Please select an option (1-3): ").strip()
        match user_input:
            case "1":
                user_search_name = input("Please input name here: ").strip()
                found = search_by_name(user_search_name, items)
                if(found):
                    print(found)
                else:
                    print(f"No item with the Name '{user_search_name}' was found.")
                
            case "2":
                user_search_ID = input("Please input ID here: ").strip()
                found = search_by_id(user_search_ID, items)
                if(found):
                    print(found)
                else:
                    print(f"No item with the ID '{user_search_ID}' was found.")

            case "3":
                main()
                break
            case _:
                print("Invalid please try again")

#######################################
# VALIDATION Functions for user input #
#######################################

def validate_item_id(items, message_prompt):
    while True:
        user_input_id = validate_numerical_input(message_prompt)
        item_id = search_by_id(user_input_id, items)
        if not item_id:
            return user_input_id
        print("Conflicting item ID, Please enter a unique ID.")
            
def validate_numerical_input(message_prompt):
    while True:
        user_input_numerical = input(message_prompt).strip()
        if user_input_numerical.isdigit() and user_input_numerical:
            return user_input_numerical
        print("Input must be a numerical number.")

def validate_supplier_id(message_prompt):
        suppliers = read_suppliers_from_json()
        while True:
            user_input_supplier_id = validate_numerical_input(message_prompt)
            for supplier in suppliers:
                if user_input_supplier_id == supplier['id']:
                    return user_input_supplier_id
            print("Supplier ID not found.")

#########################################
# Main to Initialize menu and item list #
#########################################

def main():
    items_file = 'items.txt'
    items = read_items_from_json()
    suppliers = read_suppliers_from_json()
    print(suppliers)
    display_main_menu(items, items_file)
  
if __name__ == "__main__":
    display_welcome_menu()
    main()