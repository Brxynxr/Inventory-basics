# We ask the user if they want to start the registration
print ("----------------INVENTORY-----------------")
register = input("do you want to register a product?: yes/no ").lower()

# The loop will run while the answer is "yes"
while register == "yes":
    name = input("enter product name: ")
    
    # Price validation
    price = None  
    # None is an empty value
    # I used it to tell the loop there is no valid data yet and it should keep asking
    
    while price == None:
        try:
            price = float(input("enter product price: "))
        except ValueError:
            print("Error: invalid data")
            
    # Quantity validation     
    quantity = None
    # Same as with price
    # Quantity starts as None (empty) so the loop keeps asking until it gets a valid number
    
    while quantity == None:
        try:
            quantity = int(input("enter number of units: "))
        except ValueError:
            print("Error: invalid data")

    # We calculate the total cost by multiplying price by quantity
    total_cost = price * quantity

    # We display the ordered summary
    print("REGISTERED PRODUCT".center(64, "-"))
    print(f"Product: {name} | Price: {price} | Quantity: {quantity} | Total: {total_cost}")
    print("-" * 64)
   
    # We ask if they want to continue to decide if the loop repeats or ends
    register = input("do you want to register another product?: yes/no ").lower()

"""
PROGRAM FUNCTION
It is a program that allows you to register products in an inventory
easily. You enter the name, price and quantity, and the system
validates the data, calculates the total cost and displays
the result on screen.
"""
