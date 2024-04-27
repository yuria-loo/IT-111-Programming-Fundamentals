# Yuria Loo
# IT111:AD4
# 2024-04-27

"""
This programs lets a user to prompt to create a jason file with some fields
that the user specified, and lets the user to search a specific data from the 
file.
"""
import json
import os

# function 1: lets a user to fill the fields and create a JSON file
# (make sure that the file name is corresponding to the order number)
def createOrder():
    # Initializes an order
    order = {}
    # Lets a user to fill the fields
    order["id"]           = input("Enter order ID: ")
    order["product_no"]   = input("Enter product number: ")
    order["product_name"] = input("Enter product name: ")
    order["price"]        = input("Enter price: ")
    order["customer_id"]  = input("Enter customer ID: ")
    # Creates a file for each order
    order_number = order["id"]
    file         = f"order_{order_number}.json"
    # Opens the file to write the order
    with open(file, "w") as json_file:
        json.dump(order, json_file)
    print(f"Order{order_number} created and saved as {file}")
    
# function 2: reads the file and searches the 
def searchOrder():
    # Lets a user to specify the file to search
    order_number = input("Enter order number to search: ")
    file = f"order_{order_number}.json"

    # Opens the file
    if os.path.exists(file):
        with open(file, "r") as json_file:
            order = json.load(json_file)
            print("Order: ")
            for key, value in order.items():
                print(f"{key}: {value}")
    else:
        print(f"Order {order_number} not found.")

# calls the functions(lets the user to choose whether they want to create the order or
#  search the order)

def main():
    # UserInterface
    print("Option Menu:")
    print("1: Create Order")
    print("2: Search Order")
    print("3: Exit from Menu")

    # User choise
    userChoise = int(input("Select the option: "))

    # Function calls based on the option
    match userChoise:
        case 1:
            createOrder()
        case 2:
            searchOrder()
        case 3:
            return
        case _:
            print("Invalid option.")

# Calls main function
main()
