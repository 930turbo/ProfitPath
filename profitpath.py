import csv
import matplotlib.pyplot as plt

# Declare variables
item_name = input("Enter the name of the item being sold: ")
list_price = float(input("Enter the list price of the item (in dollars): "))
purchase_price = float(input("Enter the purchase price of the item (in dollars): "))
sale_price = float(input("Enter the sale price of the item (in dollars): "))
sale_date = input("Enter the date of the sale (in the format YYYY-MM-DD): ")
summary = input("Enter a summary of the sale: ")
goal = int(input("Enter a sales goal for this item: "))
total_sales = 0

# Open sales records file
with open('Sales Records.csv', mode='a') as sales_file:
    sales_writer = csv.writer(sales_file)
    # Write sale information to file
    sales_writer.writerow([item_name, list_price, purchase_price, sale_price, sale_date, summary])

# Check if sales goal has been reached
total_sales += 1
if total_sales >= goal:
    print("Congratulations! You have reached your sales goal for this item!")

# Give user the option to visualize sales growth
choice = input("Would you like to visualize your sales growth? (yes/no)")
if choice == "yes":
    # Read the sales data from file
    data = []
    with open("Sales Records.csv", "r") as sales_file:
        csv_reader = csv.reader(sales_file)
        for row in csv_reader:
            data.append(row)
    
    # Extract sale prices from the data
    sale_prices = [row[3] for row in data[1:]]
    sale_dates = [row[4] for row in data[1:]]

    # Visualize the sales data
    plt.plot(sale_dates, sale_prices)
    plt.xlabel("Sale Date")
    plt.ylabel("Sale Price")
    plt.title("Sales Growth")
    plt.show()
